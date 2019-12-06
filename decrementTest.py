from packages.SellItem import SellItem
from packages.User import User
from packages.Watcher import Watcher
import threading
import time
print('users will be created')
try:
    user1=User('furkan@gmail.com', 'furkan akyol', '123abc123')
    user2=User('azad@gmail.com', 'azad', '123abc123')
    user3=User('yusuf@gmail.com', 'yusuf', '123abc123')
except:
    raise ValueError('error while creating user instances')

print(user1.name_surname+' has been created')
print(user2.name_surname+' has been created')
print(user3.name_surname+' has been created\n')



print('SellItems will be created')
period=5 # dakika olarak olcakmis degistiririz
delta=10
stop=20
starting_price=100
try:
    sellitem1=SellItem(user3, 'iphone x', 'phone','desc',('decrement',period,delta,stop), starting_price)
except:
    raise ValueError('error while creating sellItems')

print(sellitem1.title+' sellitem has been created')


# -----------------------------------------auction starts---------------------------------------------------
sellitem1.start_auction()

#this method will check if price decremented at every period
time.sleep(0.5)
i=1
def checkprice():
    global i
    if sellitem1.state == 'sold':
        return 1

    if(sellitem1.current_price!=(starting_price-i*delta)):
        print('current price is '+str(sellitem1.current_price)+' and it is wrong')
    else:
        print('current price is '+str(sellitem1.current_price)+' and it is true')    
    i+=1
    timer=threading.Timer(period, checkprice)
    timer.start()
    timer.join()
    
timer=threading.Timer(period, checkprice)
timer.start()



print('\n\n\n\n\n\nTEST FOR AUCTION')
user1.add_balance(10)#20 
user2.add_balance(50)#60


sellitem1.bid(user1,10)
if(10==user1.balance-user1.reserved):
    pass
else:
    raise ValueError('reserve is wrong')


sellitem1.bid(user2,40)
if(20==user2.balance-user2.reserved):
    pass
else:
    raise ValueError('reserve is wrong')

timer.join()

print(sellitem1.history())
