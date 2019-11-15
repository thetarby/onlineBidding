class SellItem:
    def __init__(self,owner,title,item_type,decsription,bidtype,starting,minbid,watcher,image):
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
        self.amount=minbid
        self.state = 'active'
        self.history={
            'start_price':self.minbid, # minbid mi başlangıç fiyatı emin olamadım?????,
            'selling_price':0,
            'bid_history':[] # a list of pairs which is (amount,user_who_paid_it)
        }

    def start_auction(self, topbid=None):
        self.watcher.notify(self.item_type)
        self.state = 'onhold'
        self.watcher.notify(self)

    
    def bid(self, user, amount):
        if amount <= self.amount:
            raise ValueError('Amount should be more than the last bid')
        if self.state == 'sold':
            raise ValueError('Auction is not active')
        if user.get_balance() - user.get_reserved() < amount:
            raise ValueError('Cannot bid that much amount')
        
        # burda iki tane boşluk vardı hayırdır yeni fonskiyon mu bu???? ben de öyle düşünmüştüm.
        self.highest_payer = user
        self.history['bid_history'].append((self.amount,user))
        self.amount = amount
        self.watcher.notify(self)


   """
    burda ownerı bilgilendirmemiz lazım senin itemin satıldı diye
    o da itemi satılan itemlerine ekliycek böylece
    bunu nasıl yaparız düşünelim. Bi item classı yaratmak sanki 
    işimize yarıcak gibi genel olarak.
   """     
    def sell(self):
        self.highest_payer.buy(self.item_type,self.amount)
        self.state = 'sold'
        self.history['selling_price']=self.amount
        self.watcher.notify(self)

    
    def view(self):
        print('owner: ', self.owner)
        print('title: ', self.title)
        print('item_type: ', self.item_type)
        print('description: ', self.decsription)
        print('bidtype: ', self.bidtype)
        print('starting: ', self.starting)
        print('minbid: ', self.minbid)


    def watch(self, user,method):
        self.watcher.item_watcher_register(self,user,method)


    def history(self):    
        return self.history

    def get_item_type(self):
        return self.item_type
    
    def get_state(self):
        return self.state