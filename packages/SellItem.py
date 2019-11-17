class SellItem:
    def __init__(self,owner,title,item_type,decsription,bidtype,starting,watcher,minbid=1.0,image=None):
        self.owner=owner
        self.title=title
        self.item_type=item_type
        self.decsription=decsription
        self.bidtype=bidtype
        self.starting=starting
        self.minbid=minbid
        self.image=image
        self.watcher=watcher
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


    def start_auction(self, stopbid=None):
        self.watcher.notify(self.item_type)
        self.watcher.notify(self)
        if stopbid is not None:
            self.stopbid = stopbid
        else:
            print('stopbid is not defined')

    
    def bid(self, user, amount):
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
            user.buy(self, self.item_type, amount)
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
