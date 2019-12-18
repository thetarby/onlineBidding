# from packages.SellItem import *
from packages.SellItem import SellItemBase
import time
class SellItemIncrement(SellItemBase):
    def __init__(self,owner,title,item_type,decsription,bidtype,starting,minbid=1.0,image=None):
        super().__init__(owner,title,item_type,decsription,bidtype,starting,minbid,image)
        self.min_delta = bidtype[1]
        self.instantsell = bidtype[2]

    
    #override
    @SellItemBase.require_lock
    def bid(self, user, amount):
        time.sleep(10)
        if amount < self.last_bid + self.min_delta:
            return('Amount should be more than the last bid plus min_delta')
        if self.state == 'sold':
            return('item is sold')
        if user.get_balance() - user.get_reserved() < amount:
            return('Cannot bid that much amount')
        if self.state == 'active':
            self.state = 'onhold'
            self.history_['start_price'] = amount

        old_user=self.highest_payer
        if(old_user is not None): old_user.take_bid_back(self.last_bid)
        
        self.highest_payer = user
        self.last_bid = amount
        self.history_['bid_history'].append((amount,user.email))
        user.reserve(amount)
        if amount >= self.instantsell:
            self.sell()
        #item state'i değiştiği içiin izleyenleri notify et
        self.watcher.notify(self)
        return 1