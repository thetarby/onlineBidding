from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.FloatField(default=0)
    reserved = models.FloatField(default=0)
    email = models.EmailField(max_length=150)
    name_surname= models.CharField(max_length=100, blank=True)

    def reserve(self,amount):
        if self.balance>=amount:
            self.balance-=amount
            self.reserved+=amount
            self.save()
            return 1
        else:
            return 0

    def add_balance(self,amount):# TODO: eksili balance eklemeye bak
        new_balance = self.balance + amount
        if new_balance < 0:
            print('You cannot withdraw {}'.format(amount))
        else:
            self.balance+=amount
            self.save()

    def buy(self,item,item_type,price):
        if price > self.balance+self.reserved:
            print('Not enough money to buy')
        else:
            print('YARRAMI YEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEee')
            self.reserved -= price
            item.owner=self
            item.save()
            #self.owned_items[item_type].append(item.id)
            #self.financial_report['expenses'].append((item.id, price))

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance, email=instance.email, name_surname=instance.fullname)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.userprofile.save()