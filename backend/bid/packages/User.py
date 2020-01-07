import re
import random
from packages.Watcher import Watcher

class User:
    def __init__(self,email,name_surname,password):
        self.email=email
        self.name_surname=name_surname
        self.password=password
        self.balance=10 #yeni üyeye kıyak kanka
        self.watcher=Watcher()
        self.owned_items={}
        self.enable = False
        self.financial_report = {
            'items_sold': [],
            'items_on_sale': [],
            'expenses': [],
            'income': []
            }
        self.reserved = 0
        self.verification_number = 'A1B1C1'

    def verify(self,verification_number):
        email_form = '^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$'
        if re.match(email_form, self.email) != None:
            if verification_number == self.verification_number:
                self.enable = True
                return 1
            else:
                return('Wrong verification number')
        else:
            return('Enter a valid email address')          


    def change_password(self,new_password,old_password=None):
        if(old_password is not None):
            if(old_password==self.password):
                self.password=new_password
                return 1
            else:
                return('Old password is not correct.')
        else:
            return('Please look at your mail')


    def list_items(self, item_type=None, state='all'):
        items = []
        if item_type == None:   # list all item types
            if state == 'all':
                for itype in self.owned_items:
                    items += self.owned_items[itype]
            else:
                for itype in self.owned_items:
                    items += filter(lambda x: x.get_state() == state, self.owned_items[itype])
        else:
            if state == 'all':
                items += self.owned_items[item_type]
            else:
                items += filter(lambda x: x.get_state() == state, self.owned_items[item_type])
        
        return items


    def watch(self,watch_method,item_type=None):
        return self.watcher.register(self, watch_method,item_type)


    def add_balance(self,amount):
        if self.balance + amount < 0:
            return('You cannot withdraw {} dollars'.format(-amount))
        else:
            self.balance=self.balance+amount
            return 1

    
    def buy(self,item,item_type,price):
        if price > self.balance:
            print('Not enough money to buy')
        else:
            self.balance -= price
            self.reserved -= price
            if(item_type not in self.owned_items):
                self.owned_items[item_type]=[]
            self.owned_items[item_type].append(item.id)
            self.financial_report['expenses'].append((item.id, price))
        

    def report(self):
        return self.financial_report


    def get_balance(self):
        return self.balance


    def get_reserved(self):
        return self.reserved
    
    
    def reserve(self,amount):
        if(amount<=self.balance-self.reserved):
            self.reserved+=amount
            return 1
        else:
            return 0        


    def take_bid_back(self, bid_amount):
        self.reserved -= bid_amount

    
    def item_sold(self, item):
        self.financial_report['items_sold'].append(item.id)
        self.financial_report['items_on_sale'].remove(item.id)
        self.financial_report['income'].append((item.id, item.history_['selling_price']))
    
