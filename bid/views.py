from django.shortcuts import render
from .models import SellItem,SellItemDecrement,SellItemIncrement,Item,Messages
from django.contrib.auth.models import User
from bid.models import WatchSell
from django.db import transaction

# Create your views here.
def home(request):
    if request.method=='GET':
        sells=[sell for sell in SellItem.objects.filter(state='active')]
        context={
            'sells':sells
        }
        print(request)
        return render(request,'bid/home.html',context)
    else:
        user = request.user
        if not WatchSell.objects.filter(user__id=user.userprofile.id):
            item_id = int(request.POST['item_id'])
            sellitem = SellItem.objects.filter(state='active').get(item__id=item_id)
            WatchSell(user=request.user.userprofile, sell=sellitem).save()
            sells=[sell for sell in SellItem.objects.filter(state='active')]
            context={
                'sells':sells,
                'messages': ['Item is being watched.']
            }
            print(request)
            return render(request,'bid/home.html',context)
        else:
            sells=[sell for sell in SellItem.objects.filter(state='active')]
            context={
                'sells':sells,
                'messages': ['Item is already being watched']
            }
            print(request)
            return render(request,'bid/home.html',context)



def messages(request):
    messages=[mes.message for mes in Messages.objects.filter(user__id=request.user.userprofile.id)]
    return render(request, 'bid/messages.html', {'notification_messages':messages})


@transaction.atomic
def bid_screen(request,item_id):
    if request.method=='GET':
        sell=SellItem.objects.filter(state='active',item__id=item_id).first()
        context={
            'sell':sell
        }
        return render(request,'bid/bid_screen.html',context)
    else:
        amount=int(request.POST['amount'])
        user=User.objects.all().filter(id=request.user.id).select_related('userprofile').first().userprofile
        item=int(request.POST['item_id'])
        if(hasattr(SellItem.objects.filter(state='active').get(item__id=item),'sellitemdecrement' )):
            print('decrement bidding')
            res=SellItem.objects.filter(state='active').get(item__id=item).sellitemdecrement.bid(user,amount)
        elif(hasattr(SellItem.objects.filter(state='active').get(item__id=item),'sellitemincrement' )):
            print('increment bidding')
            res=SellItem.objects.filter(state='active').get(item__id=item).sellitemincrement.bid(user,amount)
        elif(hasattr(SellItem.objects.filter(state='active').get(item__id=item),'selliteminstantincrement' )):
            print('instant increment bidding')
            res=SellItem.objects.filter(state='active').get(item__id=item).selliteminstantincrement.bid(user,amount)
        sell=SellItem.objects.filter(state='active',item__id=item_id).first()
        context={
            'sell':sell,
            'messages':['You bidded succesfully' if res==1 else res]
        }
        return render(request,'bid/bid_screen.html',context)