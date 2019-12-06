# from packages.SellItem import *
from packages.SellItem import SellItemBase

class SellItemInstantIncrement(SellItemBase):
    def __init__(self,owner,title,item_type,decsription,bidtype,starting,minbid=1.0,image=None):
        super().__init__(owner,title,item_type,decsription,bidtype,starting,minbid,image)
        self.bidded_users={}
        self.total_bid=0
        self.minbid = bidtype[1]
        self.autosell = bidtype[2]


    # TODO: eğer adam en çok teklif edenden daha az verirse yine de bid kabul edilcek mi?
    # senaryoya bagli kanka. eger insanlar kim ne kadar vermis bilmiyorsa kim ne veriyorsa kosulsuz almak lazim
    # eger last_bid diye en yuksek mebla bilincekse daha dusuk verirlerse kabul etmeyek sacma olur
    #override
    def bid(self,user,amount):
        if(user not in self.bidded_users):
            self.bidded_users[user]=0
        if self.state == 'sold':
            print('item is already sold')
            return 0
        if user.get_balance() - user.get_reserved() < amount:
            print('{} does not have {} in account'.format(user.name_surname, amount))
            return 0
        if amount<self.minbid or self.last_bid>=(self.bidded_users[user]+amount):
            print('{} should bid more than {}'.format(user.name_surname, amount))
            return 0
        if self.state == 'active':
            self.state = 'onhold'
            self.history_['start_price'] = amount

        # kardo simdi onceden 50 veren bu sefer 20 verirse toplam 70 vermis gibi mi dusuncez
        # last bid ile kiyaslarken? ve history'e eklerken 70 verdi mi diyecez yoksa 20 mi?
        self.highest_payer = user
        self.history_['bid_history'].append((amount,user))
        self.bidded_users[user]+=amount
        self.last_bid=self.bidded_users[user]
        self.total_bid+=amount
        user.reserve(amount)    

        #auto sell is reached
        if(self.total_bid>=self.autosell):
            self.sell() 
            print('{} is sold to {} with a total amount of {}'.format(self.title, user.name_surname, self.total_bid))
        print('{} bidded {}'.format(user.name_surname, amount))
        return 1


    def sell(self):
        for user in self.bidded_users:
            bid=self.bidded_users[user]
            user.reserved-=bid
            user.add_balance(-bid)

        self.highest_payer.buy(self,self.item_type,self.last_bid)
        self.state = 'sold'
        self.history_['selling_price']=self.last_bid
        self.watcher.notify(self)
        self.owner.item_sold(self)    
