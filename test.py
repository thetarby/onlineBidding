from packages.SellItem import *
from packages.User import *
from packages.watcher import *


"""
    -------------------------TEST FOR CONSTRUCTORS-----------------------------
"""
print('Watcher will be created')
try:
    watcher=Watcher()
except:
    raise ValueError('error while creating watcher instance')    


print('users will be created')
try:
    user1=User('asd@gmail.com', 'furkan akyol', '123abc123', watcher)
    user2=User('ass@gmail.com', 'azad', '123abc123', watcher)
    user3=User('asc@gmail.com', 'yusuf', '123abc123', watcher)
except:
    raise ValueError('error while creating user instances')    

print('a user with invalid e-mail is trying to be created, should be rejected')
user4=User('asgmail.com', 'at akyol', '123abc123', watcher)
user4.verify('123abc123')
if(user4.enable):
    raise ValueError('user with invalid e-mail should not have been created')

print(user1.name_surname+' is created')
print(user2.name_surname+' is created')
print(user3.name_surname+' is created')


print('SellItems will be created')
try:
    sellitem1=SellItem(user1, 'iphone x', 'telefon','desc','bidtype', 'starting',watcher)
    sellitem2=SellItem(user1, 'iphone 5s', 'telefon', 'desc','bidtype','starting',watcher)
    sellitem3=SellItem(user1, 'mercedes c coupe 2 kapılı', 'car', 'desc','bidtype','starting',watcher)
except:
    raise ValueError('error while creating user instances')

"""
    -------------------------END OF TEST FOR CONSTRUCTORS-----------------------------
"""




"""
    -------------------------TEST FOR WATCH METHODS-----------------------------
"""

"""
    This method is to be called with user1 when a telefon item is on sale
    If it is called with another user who is not watching telefon items
    test fails
"""
def f(user):
    if(user.name_surname!=user1.name_surname):
        raise ValueError('watch method called with wrong user')
    print(user.name_surname+' is notified since he is watching phone items')


"""
    This method is to be called with user3 when a car item is on sale
    If it is called with another user who is not watching car items
    test fails
"""
def g(user):
    if(user.name_surname!=user3.name_surname):
        raise ValueError('watch method called with wrong user')
    print(user.name_surname+' is notified since he is watching car items')


print('user1 will watch phone items')
try:
    user1.watch(lambda :f(user1), 'telefon')
except:
    raise ValueError('error while calling watch method of user class')


print('user3 will watch car items')
try:
    user3.watch(lambda :g(user3), 'car')
except:
    raise ValueError('error while calling watch method of user class')

print('user3 will watch car items again it should be rejected and None returned')
try:
    t=user3.watch(lambda :g(user3), 'car')
    if(t == 0):
        print('passed')
    else:
        raise ValueError('user3 cannot watch an item twice')
except:
    raise ValueError('error while calling watch method of user class')


print('a phone item will be on sale')
try:
    sellitem1.start_auction()
except:
    raise ValueError('error while starting auction')


print('a car item will be on sale')
try:
    sellitem3.start_auction()
except:
    raise ValueError('error while starting auction')

"""
    -------------------------END OF TEST FOR WATCH METHODS-----------------------------
"""









"""
    -------------------------TEST FOR SELLITEM-----------------------------
"""
user1.add_balance(10)#20 
user2.add_balance(50)#60

sellitem1.bid(user1,10)
if(10==user1.balance-user1.reserved):
    pass
else:
    raise ValueError('reserve is wrong')


#should be rejected since it is lower than last bid
x=sellitem1.bid(user2,8)
if(x==0): pass
else: raise ValueError('bid should have been rejected')

if(60==user2.balance-user2.reserved):
     pass
else:
    raise ValueError('reserve is wrong')   

sellitem1.bid(user2,15)
if(45==user2.balance-user2.reserved):
    pass
else:
    raise ValueError('reserve is wrong')

#should be rejected since user1 does not have that much money
x=sellitem1.bid(user1, 30)
if(x==0): pass
else: raise ValueError('bid should have been rejected')


if(20==user1.balance-user1.reserved):
    pass
else:
    raise ValueError('reserve is wrong')

"""
    -------------------------END OF TEST FOR WATCH METHODS-----------------------------
"""


print('all tests are succesful \ngrade:100\ngood job\nkeep it up!!!')
