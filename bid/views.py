from django.shortcuts import render
from .models import SellItem,SellItemDecrement,SellItemIncrement,Item,Messages
from django.contrib.auth.models import User


# Create your views here.
def home(request):
    sells=[sell for sell in SellItem.objects.filter(state='active')]
    context={
        'sells':sells
    }
    print(request)
    return render(request,'bid/home.html',context)


def messages(request):
    messages=[mes.message for mes in Messages.objects.filter(user__id=request.user.userprofile.id)]
    return render(request, 'bid/messages.html', {'notification_messages':messages})

def bid_screen(request,item_id):
    if request.method=='GET':
        item=Item.objects.filter(id=item_id).first()
        print(item)
        context={
            'item':item
        }
        return render(request,'bid/bid_screen.html',context)
    else:
        amount=int(request.POST['amount'])
        user=User.objects.all().filter(id=request.user.id).select_related('userprofile').first().userprofile
        item=int(request.POST['item_id'])
        if(hasattr(SellItem.objects.filter(state='active').get(item__id=item),'sellitemdecrement' )):
            res=SellItem.objects.filter(state='active').get(item__id=item).sellitemdecrement.bid(user,amount)
        elif(hasattr(SellItem.objects.filter(state='active').get(item__id=item),'sellitemincrement' )):
            print('bidding')
            res=SellItem.objects.filter(state='active').get(item__id=item).sellitemincrement.bid(user,amount)
        item=Item.objects.filter(id=item_id).first()
        context={
            'item':item,
            'messages':['You bidded succesfully' if res==1 else res]
        }
        return render(request,'bid/bid_screen.html',context)