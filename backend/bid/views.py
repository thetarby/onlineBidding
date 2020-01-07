from django.shortcuts import render
from django.http import HttpResponse
from .models import SellItem,SellItemDecrement,SellItemIncrement,Item,Messages
from django.contrib.auth.models import User
import json
from django.core import serializers
#serializers
def user_profile_serializer(item):
    r = {}
    for i in ['balance','reserved','name_surname']:
        r[i] = getattr(item,i)
    return r
def item_serializer(item):
    r = {}
    for i in ['id','title','description','item_type']:
        r[i] = getattr(item,i)
    r['owner']=user_profile_serializer(item.owner)
    return r
def sell_serializer(sells):
    r = []
    for sell in sells:
        d={}
        for i in ['starting','current_price','state']:
            d[i] = getattr(sell,i)
        d['item'] = item_serializer(sell.item)
        r.append(d)
    return r



# Create your views here.


# Function: success(obj,name)
# Return a successfull result in JSON httpresponse
def success(obj, name):
	return HttpResponse(json.dumps({'result':'Success',name : obj}),
				'text/json')

# Function: error(reason)
# Return a successfull result in JSON
def error(reason):
	return HttpResponse(json.dumps({'result':'Fail','reason' : reason}),
				'text/json')

def test(request):
    print(request.user)
    sells=[sell for sell in SellItem.objects.filter(state='active')]
    return(success(sell_serializer(sells), 'data'))

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
            print('decrement bidding')
            res=SellItem.objects.filter(state='active').get(item__id=item).sellitemdecrement.bid(user,amount)
        elif(hasattr(SellItem.objects.filter(state='active').get(item__id=item),'sellitemincrement' )):
            print('increment bidding')
            res=SellItem.objects.filter(state='active').get(item__id=item).sellitemincrement.bid(user,amount)
        elif(hasattr(SellItem.objects.filter(state='active').get(item__id=item),'selliteminstantincrement' )):
            print('instant increment bidding')
            res=SellItem.objects.filter(state='active').get(item__id=item).selliteminstantincrement.bid(user,amount)
        item=Item.objects.filter(id=item_id).first()
        context={
            'item':item,
            'messages':['You bidded succesfully' if res==1 else res]
        }
        return render(request,'bid/bid_screen.html',context)