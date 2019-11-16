from packages.SellItem import *
from packages.User import *
from packages.watcher import *

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


print('SellItems will be created')
try:
    sellitem1=SellItem(user1, 'iphone x', 'telefon','desc','bidtype', 'starting',watcher)
    sellitem2=SellItem(user1, 'iphone 5s', 'telefon', 'desc','bidtype','starting',watcher)
    sellitem3=SellItem(user1, 'mercedes c coupe 2 kapılı', 'araba', 'desc','bidtype','starting',watcher)
except:
    raise ValueError('error while creating user instances')

"""
    This method is to be called with user1 when a telefon item is on sale
    If it is called with another user who is not watching telefon items
    test fails
"""
def f(user):
    if(user.name_surname!=user1.name_surname):
        raise ValueError('watch method called with wrong user')
    print(user.name_surname+' is notified')


print('user1 is watching telefon items')
try:
    user1.watch(lambda :f(user1), 'telefon')
except:
    raise ValueError('error while calling watch method of user class')


print('a telefon item will be on sale')
try:
    sellitem1.start_auction()
except:
    raise ValueError('error while starting auction')


print('test is succesful')
