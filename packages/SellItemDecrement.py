from packages.SellItem import *


class SellItemDecrement(SellItemBase):
    def __init__(self,owner,title,item_type,decsription,bidtype,starting,minbid=1.0,image=None):
        super().__init__(owner,title,item_type,decsription,bidtype,starting,minbid,image)
        self.current_price=starting
        self.period = bidtype[1]
        self.delta=bidtype[2]
        self.stop_decrement=bidtype[3]

    def _start_timer(self,period,callback):
        self.timer=threading.Timer(period, callback)
        self.timer.start()
  

    # def _decrement_handler(self):
    #     print("asdasdasd")
    #     self.current_price-=self.delta # TODO: check if it is less than zero
    #     if(self.current_price==self.stop_decrement):
    #         self.sell() # TODO: there might not be any customer check that case.
    #         return 1
    #     elif(self.current_price<self.last_bid):
    #         self.sell()
    #         return 1    
    #     #if not sold reset timer    
    #     self._start_timer(self.period, self._decrement_handler)
    #     return 0
    def _decrement_handler(self):
        print("asdasdasd")
        new_price = self.current_price - self.delta
        if new_price > self.stop_decrement and new_price > 0:
            self.current_price=new_price
            if self.current_price <= self.last_bid:
                self.sell()
                return 1
            else:
                self._start_timer(self.period, self._decrement_handler)
                return 0
        elif self.current_price <= self.last_bid:
            self.sell()
            return 1
        else:
            # sure bitti ve alan cikmadi. satmadan bitir
            self.state = 'inactive'
            return 0


    #override
    def start_auction(self):
        self.state = 'active'
        self.watcher.notify(self.item_type)
        self.watcher.notify(self)
        self._start_timer(self.period, self._decrement_handler)

    # AZAD: decrement icin bid'i degistirmeyecez sanki?
    #override
    def bid(self, user, amount):# TODO: check starting price for the first bid
        if amount <= self.last_bid:
            print('Amount should be more than the last bid')
            return 0
        if self.state == 'sold' or self.state == 'inactive':
            print('item is sold or inactive')
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
        self.history_['bid_history'].append((self.last_bid,user)) # AZAD: last_bid onceki adamin yenisiyle degistircez
        self.last_bid = amount
        user.reserve(amount)
        if amount >= self.current_price:
            self.sell()
        #item state'i değiştiği içiin izleyenleri notify et
        self.watcher.notify(self)
        return 1