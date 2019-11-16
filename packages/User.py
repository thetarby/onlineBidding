import re
import random

class User:
    def __init__(self,email,name_surname,password,watcher):
        self.email=email
        self.name_surname=name_surname
        self.password=password
        self.balance=10 #yeni üyeye kıyak kanka
        self.watcher=watcher
        self.owned_items={}
        self.enable = False
        self.financial_report = {
            'items_sold': [],
            'items_on_sale': [],
            'expenses': [],
            'income': []
            }
        self.reserved = 0
        self.verification_number = password # we set it to password for test purposes


    def verify(self,verification_number):
        email_form = '^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$'
        if re.match(email_form, self.email) != None:
            if verification_number == self.verification_number:
                self.enable = True
            else:
                print('Wrong verification number')
        else:
            print('Enter a valid email address')          


    def change_password(self,new_password,old_password=None):
        if(old_password is not None):
            if(old_password==self.password):
                self.password=new_password
            else:
                raise ValueError('Old password is not correct.')
        else:
            self.password=new_password


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
        self.balance=self.balance+amount

    
    def buy(self,item,item_type,price):
        if price > self.balance:
            raise ValueError('Not enough money')

        self.balance -= price
        self.reserved -= price
        if(item_type not in self.owned_items):
            self.owned_items[item_type]=[]
        self.owned_items[item_type].append(item)
        self.financial_report['expenses'].append((item, price))
    

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
        self.financial_report['items_sold'].append(item)
        self.financial_report['items_on_sale'].remove(item)
        self.financial_report['income'].append((item, item.history_['selling_price']))
