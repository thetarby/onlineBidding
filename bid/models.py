from django.db import models
from django.contrib.auth.models import User
from users.models import UserProfile
import threading
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib import messages
# Create your models here.sv
class BiddedUser(models.Model):
    bidded_user=models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    bid=models.FloatField(default=0)

    def update_bid(self, amount):
        self.bid+=amount
        return self.save()



class Item(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    owner=models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    item_type=models.CharField(max_length=100)


class SellItem(models.Model):
    item=models.OneToOneField(Item ,on_delete=models.CASCADE)
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
        self.save()
        #item state'i değiştiği içiin izleyenleri notify et
        #self.watcher.notify(self)
        return 1


class SellItemInstantIncrement(SellItem):
    total_bid=models.FloatField(default=0)
    minbid=models.FloatField(default=0)
    last_bid=models.FloatField(default=0)

    def start_auction(self):
        self.state = 'active'
        #self.watcher.notify(self.item_type)
        #self.watcher.notify(self)
        self.save()


    def bid(self, user, amount):
        if self.state == 'sold':
            return('item is already sold')
        if user.balance < amount:
            return('{} does not have {} in account'.format(user.name_surname, amount))

        bidded_user = BiddedUser.objects.filter(bidded_user__id=user.id)
        if not bidded_user:
            bidded_user = BiddedUser(bidded_user=user, bid=0)
            bidded_user.save()
        
        if amount<self.minbid or self.last_bid>=(bidded_user.bid+amount):
            return('{} should bid more than {}'.format(user.name_surname, amount))
        # if self.state == 'active':
        #     self.state = 'onhold'
        #     self.history_['start_price'] = amount

        self.highest_payer = user
        # self.history_['bid_history'].append((amount,user.email))
        bidded_user.update_bid(amount)
        self.last_bid=bidded_user.bid + amount
        self.total_bid+=amount
        user.reserve(amount)

        #auto sell is reached
        if(self.total_bid>=self.current_price):
            self.sell()
            print('{} is sold to {} with a total amount of {}'.format(self.title, user.name_surname, self.total_bid))
        print('{} bidded {}'.format(user.name_surname, amount))
        self.save()
        return 1
    

    def sell(self):
        self.highest_payer.buy(self.item,self.item.item_type,self.total_bid)
        self.state = 'sold'
        #self.history_['selling_price']=self.last_bid
        #self.watcher.notify(self)
        self.save()
        #self.owner.item_sold(self)

class SellItemDecrement(SellItem):
    period=models.FloatField(blank=False)
    delta=models.FloatField(blank=False)
    stop_decrement=models.FloatField(default=0)
    last_bid=models.FloatField(default=0)


    def start_auction(self):
        self.state = 'active'
        #self.watcher.notify(self.item_type)
        #self.watcher.notify(self)
        self._start_timer(self.period, self._decrement_handler)
        self.save()


    def _start_timer(self,period,callback):
        self.timer=threading.Timer(period, callback)
        self.timer.start()
  

    def _decrement_handler(self):
        print("decrement")
        print(self.state)
        new_price = self.current_price - self.delta
        if(self.state!='active'):
            return 1
        if new_price > self.stop_decrement and new_price > 0:
            print(new_price)
            self.current_price=new_price
            self.save()
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
            self.save()
            return 0


    def bid(self, user, amount):# TODO: check starting price for the first bid
        if amount <= self.last_bid:
            return('Amount should be more than the last bid')
        if self.state == 'sold' or self.state == 'inactive':
            return('item is sold or inactive')
        if user.balance < amount:
            return('Cannot bid that much amount')
        if self.state == 'active':
            self.state = 'onhold'


        old_user=self.highest_payer
        if(old_user is not None): old_user.reserve(-self.last_bid)
        
        self.highest_payer = user
        self.last_bid = amount
        #self.history_['bid_history'].append((amount,user.email)) # AZAD: last_bid onceki adamin yenisiyle degistircez
        user.reserve(amount)
        if amount >= self.current_price:
            self.sell()
        #item state'i değiştiği içiin izleyenleri notify et
        #self.watcher.notify(self)

        return 1


class WatchSell(models.Model):
    user=models.ForeignKey(UserProfile,on_delete=models.CASCADE, null=False,blank=False)
    sell=models.ForeignKey(SellItem,on_delete=models.CASCADE, null=False,blank=False)


    def notify_wathers(self,sell):
        for watch in WatchSell.objects.filter(sell_id=sell.id):
            print(watch.user.name_surname + ' will be notified.')


class WatchItemTypes(models.Model):
    user=models.ForeignKey(UserProfile,on_delete=models.CASCADE, null=False,blank=False)
    item_type=models.CharField(max_length=100,null=False, blank=False)


@receiver(post_save, sender=SellItemIncrement)
@receiver(post_save, sender=SellItemDecrement)
def notify_item_type_wathers(sender, instance, **kwargs):
    for watch in WatchItemTypes.objects.filter(item_type=instance.item.item_type):
        print(watch.user.name_surname + ' will be notified.(item type watcher)')


@receiver(post_save, sender=SellItemIncrement)
@receiver(post_save, sender=SellItemDecrement)
def notify_sell_wathers(sender, instance, **kwargs):
    for watch in WatchSell.objects.filter(sell__id=instance.id):
        print(watch.user.name_surname + ' will be notified.(sell watcher)')


