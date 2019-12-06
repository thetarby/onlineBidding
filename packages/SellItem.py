from packages.Watcher import Watcher
import threading

#sell item factory
def SellItem(owner,title,item_type,decsription,bidtype,starting,minbid=1.0,image=None):
    if(bidtype[0]=='increment'):
        return SellItemIncrement(owner,title,item_type,decsription,bidtype,starting,minbid,image)
    elif(bidtype[0]=='decrement'): 
        return SellItemDecrement(owner,title,item_type,decsription,bidtype,starting,minbid,image)
    elif(bidtype[0]=='instant increment'): 
        return SellItemInstantIncrement(owner,title,item_type,decsription,bidtype,starting,minbid,image)


class SellItemBase:
    def __init__(self,owner,title,item_type,decsription,bidtype,starting,minbid,image):
        self.owner=owner
        self.title=title
        self.item_type=item_type
        self.decsription=decsription
        self.bidtype=bidtype
        self.starting=starting
        self.minbid=minbid
        self.image=image
        self.watcher=Watcher()
        self.highest_payer=None
        self.last_bid=minbid
        self.state = 'active'
        self.history_={
            'start_price':self.minbid, # minbid mi başlangıç fiyatı emin olamadım?????,
            'selling_price':0,
            'bid_history':[] # a list of pairs which is (amount,user_who_paid_it)
        }
        self.stopbid = 0
        owner.financial_report['items_on_sale'].append(self)

    """
    def _start_timer(self,period,callback):
        self.timer=threading.Timer(period, callback)
        self.timer.start()
    """

    """
    def _decrement_handler(self):
        self.current_price-=self.delta # TODO: check if it is less than zero
        if(self.current_price==self.stop_decrement):
            self.sell() # TODO: there might not be any customer check that case.
            return 1
        else:
            self._start_timer(self.bidtype[1], self._decrement_handler)
            return 0
    """

    """
    # TODO: eğer adam en çok teklif edenden daha az verirse yine de bid kabul edilcek mi?
    def _instant_increment_handler(self,user,amount):
        if self.state == 'sold':
            print('Auction is not active')
            return 0
        if user.get_balance() - user.get_reserved() < amount:
            print('Cannot bid that much amount')
            return 0
        if self.bidded_users[self.highest_payer]<=(self.bidded_users[user]+amount):
            print('you should bid more')
            return 0
        if(amount<self.bidtype[1]):
            print('bid is less than mindelta')
            return 0
        if self.state == 'active':
            self.state = 'onhold'
            self.history_['start_price'] = amount


        old_user=self.highest_payer
        self.highest_payer = user
        self.history_['bid_history'].append((amount,user))
        self.bidded_users[user]+=amount
        self.last_bid=self.bidded_users[user]
        self.total_bid+=amount
        user.reserve(amount)    

        #auto sell is reached
        if(self.total_bid>=self.bidtype[2]):
            self.sell() 
        
        return 1
    """
    
    def start_auction(self, stopbid=None):
        pass
    
    
    def bid(self, user, amount):# TODO: check starting price for the first bid
        if amount <= self.last_bid:
            print('Amount should be more than the last bid')
            return 0
        if self.state == 'sold':
            print('Auction is not active')
            return 0
        if user.get_balance() - user.get_reserved() < amount:
            print('Cannot bid that much amount')
            return 0
        if self.state == 'active':
            self.state = 'onhold'
            self.history_['start_price'] = amount

        old_user=self.highest_payer
        if(old_user is not None): old_user.take_bid_back(self.last_bid)
        
        self.highest_payer = user
        self.history_['bid_history'].append((self.last_bid,user))
        self.last_bid = amount
        user.reserve(amount)
        if amount >= self.stopbid:
            self.sell()
        #item state'i değiştiği içiin izleyenleri notify et
        self.watcher.notify(self)
        return 1

    """
    burda ownerı bilgilendirmemiz lazım senin itemin satıldı diye
    o da itemi satılan itemlerine ekliycek böylece
    bunu nasıl yaparız düşünelim. Bi item classı yaratmak sanki 
    işimize yarıcak gibi genel olarak.
    """     
    def sell(self):
        print('sold')
        self.highest_payer.buy(self,self.item_type,self.last_bid)
        self.state = 'sold'
        self.history_['selling_price']=self.last_bid
        self.watcher.notify(self)
        self.owner.item_sold(self)


    def view(self):
        print('owner: ', self.owner)
        print('title: ', self.title)
        print('item_type: ', self.item_type)
        print('description: ', self.decsription)
        print('bidtype: ', self.bidtype)
        print('starting: ', self.starting)
        print('minbid: ', self.minbid)
        print('auction data: ', self.history_)


    def watch(self, user,method):
        self.watcher.item_watcher_register(self,user,method)


    def history(self):    
        return self.history_


    def get_item_type(self):
        return self.item_type
    

    def get_state(self):
        return self.state


#to prevent circular dependency imports at the end of file
from packages.SellItemDecrement import *
from packages.SellItemIncrement import *
from packages.SellItemInstantIncrement import *