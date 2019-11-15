import re

class User:
    def __init__(self,email,name_surname,password,watcher):
        self.email=email
        self.name_surmane=name_surname
        self.password=password
        self.balance=10 # yeni üyeye kıyak 10 tl kanka
        self.watcher=watcher
        self.owned_items={}
        self.enable = False

    def verify(self,email,verification_number):
        email_form = '^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$'
        if re.match(email_form, email) != None:
            if verification_number == self.password:
                self.enable = True
            else:
                raise ValueError('Wrong password')
        else:
            raise ValueError('Enter a valid email address')          

    def change_password(self,new_password,old_password=None):
        if(old_password is not None):
            if(old_password==self.password):
                self.password=new_password
            else:
                print('error')
        else:
            self.password=new_password
        # kardo adam eski sifreyi vermezse direkt sifresini degistiriyoz boyle sacma degil mi?

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
        self.watcher.register(self, watch_method,item_type)

    def add_balance(self,amount):
        self.balance=self.balance+amount

    
    def buy(self,item,item_type,price):
        self.balance-=price
        if(item_type not in self.owned_items):
            self.owned_items[item_type]=[]
        self.owned_items[item_type].append(item)
    


    def report(self):
        print(1)

    
