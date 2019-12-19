from django.shortcuts import render
from .models import Item
from .models import SellItem
from django.contrib.auth.models import User


# Create your views here.
def home(request):
    items=[sell.item for sell in SellItem.objects.filter(state='active')]
    context={
        'items':items
    }
    print(request)
    return render(request,'bid/home.html',context)


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
        SellItem.objects.all().select_related('item').get(item__id=item).sellitemincrement.bid(user,amount)
        item=Item.objects.filter(id=item_id).first()
        context={
            'item':item
        }
        return render(request,'bid/bid_screen.html',context)