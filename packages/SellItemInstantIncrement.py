from packages.SellItem import *

class SellItemInstantIncrement(SellItemBase):
    def __init__(self,owner,title,item_type,decsription,bidtype,starting,minbid=1.0,image=None):
        super().__init__(owner,title,item_type,decsription,bidtype,starting,minbid,image)
        self.bidded_users={}
        self.total_bid=0

    # TODO: eğer adam en çok teklif edenden daha az verirse yine de bid kabul edilcek mi?
    #override
    def bid(self,user,amount):
        if self.state == 'sold':
            print('Auction is not active')
            return 0
        if user.get_balance() - user.get_reserved() < amount:
            print('Cannot bid that much amount')
            return 0
        if self.last_bid>=(self.bidded_users.get(user,0)+amount):
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
        if(user not in self.bidded_users):
            self.bidded_users[user]=0
        self.bidded_users[user]+=amount
        self.last_bid=self.bidded_users[user]
        self.total_bid+=amount
        user.reserve(amount)    

        #auto sell is reached
        if(self.total_bid>=self.bidtype[2]):
            self.sell() 
        
        return 1


    def sell(self):
         # if it is intant increment get money of all users
        for user,bid in self.bidded_users.keys():
            user.reserved-=bid
        self.highest_payer.buy(self,self.item_type,self.last_bid)
        self.state = 'sold'
        self.history_['selling_price']=self.last_bid
        self.watcher.notify(self)
        self.owner.item_sold(self)    

    #override
    def start_auction(self):
        self.watcher.notify(self.item_type)
        self.watcher.notify(self)  