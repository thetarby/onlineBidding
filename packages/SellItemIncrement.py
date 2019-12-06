# from packages.SellItem import *
from packages.SellItem import SellItemBase

class SellItemIncrement(SellItemBase):
    def __init__(self,owner,title,item_type,decsription,bidtype,starting,minbid=1.0,image=None):
        super().__init__(owner,title,item_type,decsription,bidtype,starting,minbid,image)
        self.min_delta = bidtype[1]
        self.instantsell = bidtype[2]

    
    #override
    def bid(self, user, amount):
        if amount < self.last_bid + self.min_delta:
            print('Amount should be more than the last bid plus min_delta')
            return 0
        if self.state == 'sold':
            print('item is sold')
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
        self.last_bid = amount
        self.history_['bid_history'].append((amount,user))
        user.reserve(amount)
        if amount >= self.instantsell:
            self.sell()
        #item state'i değiştiği içiin izleyenleri notify et
        self.watcher.notify(self)
        return 1