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


    def start_auction(self, topbid=None):
        self.watcher.notify(self.item_type)
        self.state = 'onhold'

    
    def bid(self, user, amount):
        if amount <= self.amount:
            raise ValueError('Amount should be more than the last bid')
        if self.state == 'sold':
            raise ValueError('Auction is not active')
        if user.get_balance() - user.get_reserved() < amount:
            raise ValueError('Cannot bid that much amount')
        

        self.highest_payer = user
        self.amount = amount

        
    def sell(self):
        self.highest_payer.buy(self.item_type,self.amount)
        self.state = 'sold'

    
    def view(self):
        print('owner: ', self.owner)
        print('title: ', self.title)
        print('item_type: ', self.item_type)
        print('description: ', self.decsription)
        print('bidtype: ', self.bidtype)
        print('starting: ', self.starting)
        print('minbid: ', self.minbid)


    def watch(self, user,method):
        print(1)


    def history(self):    
        print(1)

    def get_item_type(self):
        return self.item_type
    
    def get_state(self):
        return self.state