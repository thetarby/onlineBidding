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
    counter_id=0
    def __init__(self,owner,title,item_type,decsription,bidtype,starting,minbid,image):
        SellItemBase.counter_id=SellItemBase.counter_id+1
        self.id=SellItemBase.counter_id
        self.lock=threading.Lock()
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
        self.state = 'inactive'
        self.history_={
            'start_price':self.starting,
            'selling_price':0,
            'bid_history':[] # a list of pairs which is (amount,user_who_paid_it)
        }
        self.stopbid = 0
        owner.financial_report['items_on_sale'].append(self.id)


    def require_lock(f):
        def wrapper(self,*args, **kwargs):
            with self.lock:
                return f(self,*args,**kwargs)
        return wrapper
    

    def start_auction(self, stopbid=None):
        self.state = 'active'
        self.watcher.notify(self.item_type)
        self.watcher.notify(self)
    

    def bid(self, user, amount):# TODO: check starting price for the first bid
        pass

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

    @require_lock
    def view(self):
        res={
            'owner':self.owner,
            'title':self.title,
            'item_type':self.item_type,
            'description':self.decsription,
            'bidtype':self.bidtype,
            'starting': self.starting,
            'minbid':self.minbid,
            'auction data': self.history_
        }
        return res


    def watch(self, user,method):
        return self.watcher.item_watcher_register(self,user,method)


    def history(self):    
        return self.history_


    def get_item_type(self):
        return self.item_type
    

    def get_state(self):
        return self.state


#to prevent circular dependency imports at the end of file
from packages.SellItemDecrement import SellItemDecrement
from packages.SellItemIncrement import SellItemIncrement
from packages.SellItemInstantIncrement import SellItemInstantIncrement