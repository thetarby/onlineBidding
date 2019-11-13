class User:
    def __init__(self,email,name_surname,password,watcher):
        self.email=email
        self.name_surmane=name_surname
        self.password=password
        self.balance=10 # yeni üyeye kıyak 10 tl kanka
        self.watcher=watcher
        self.owned_items={}

    def verify(self,email,verification_number):
        print(1)

    def change_password(self,new_password,old_password=None):
        if(old_password is not None):
            if(old_password==self.password):
                self.password=new_password
            else:
                print('error')
        else:
            self.password=new_password

    def list_items(self, item_type=None, state='all'):
        return 1 

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

    
