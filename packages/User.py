class User:
    def __init__(self,email,name_surname,password):
        self.email=email
        self.name_surmane=name=surname
        self.password=password
        self.balance=10 # yeni üyeye kıyak 10 tl kanka


    def verify(email,verification_number):


    def change_password(new_password,old_password=None):
        if(old_password is not None):
            if(old_password==self.password):
                self.password=new_password
            else:
                print('error')
        else:
            self.password=new_password

    def list_items(user, item_type=None, state='all'):


    def watch(item_type=None, watch_method):


    def add_balance(amount):
        self.balance=self.balance+amount

    def report():    
        
