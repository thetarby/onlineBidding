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


    def start_auction(self, topbid=None):
        self.watcher.notify(self.item_type)

    
    def bid(self, user, amount):
        self.highest_payer = user
        self.amount = amount

        
    def sell(self):
        self.highest_payer.buy(self.item_type,self.amount)

    
    def view(self):
        print(1)


    def watch(self, user,method):
        print(1)


    def history(self):    
        print(1)
