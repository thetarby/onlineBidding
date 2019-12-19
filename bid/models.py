from django.db import models
from django.contrib.auth.models import User
from users.models import UserProfile
# Create your models here.sv

class Item(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    owner=models.ForeignKey(User, on_delete=models.CASCADE)
    item_type=models.CharField(max_length=100)


class SellItem(models.Model):
    item=models.ForeignKey(Item, on_delete=models.CASCADE)
    starting=models.FloatField(default=0)
    current_price=models.FloatField(default=0)
    state=models.CharField(max_length=15, default='inactive')
    highest_payer=models.ForeignKey(UserProfile, on_delete=models.CASCADE, null=True,default=None)

    def sell(self):
        self.highest_payer.buy(self.item,self.item.item_type,self.current_price)
        self.state = 'sold'
        #self.history_['selling_price']=self.last_bid
        #self.watcher.notify(self)
        self.save()
        #self.owner.item_sold(self)


class SellItemIncrement(SellItem):
    instant_sell=models.FloatField(blank=False)
    min_delta=models.FloatField(default=0)
    def bid(self, user, amount):
        print('AASDADASDASDŞLKASJDKLJASKLDJASLKDJKLSAJDKLASJ')
        if amount < self.current_price + self.min_delta:
            return('Amount should be more than the last bid plus min_delta')
        if self.state == 'sold':
            return('item is sold')
        if user.balance < amount:
            return('Cannot bid that much amount')
        if self.state == 'active':
            self.state = 'onhold'
        #    self.history_['start_price'] = amount

        old_user=self.highest_payer
        if(old_user is not None): old_user.reserve(-self.current_price)
        
        self.highest_payer = user
        self.current_price = amount
        #self.history_['bid_history'].append((amount,user.email))
        user.reserve(amount)
        if amount >= self.instant_sell:
            print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            self.sell()
        #item state'i değiştiği içiin izleyenleri notify et
        #self.watcher.notify(self)
        return 1


class SellItemBase:
    counter_id=0
    def __init__(self,item,bidtype,starting,minbid,image):
        SellItemBase.counter_id=SellItemBase.counter_id+1
        self.item=item
        self.id=SellItemBase.counter_id
        self.lock=threading.Lock()
        self.owner=item.owner
        self.title=item.title
        self.item_type=item.item_type
        self.decsription=item.description
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
        #item.owner.financial_report['items_on_sale'].append(self.id)


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
        self.highest_payer.buy(self.item,self.item_type,self.last_bid)
        self.state = 'sold'
        self.history_['selling_price']=self.last_bid
        self.watcher.notify(self)
        #self.owner.item_sold(self)

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