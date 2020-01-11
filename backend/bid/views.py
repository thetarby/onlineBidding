from django.shortcuts import render
from django.http import HttpResponse
from .models import SellItem,SellItemDecrement,SellItemIncrement,Item,Messages,WatchItemTypes,WatchSell
from django.contrib.auth.models import User
import json
from django.core import serializers
from online_bidding.serializers import *

# Create your views here.


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


def list_items(request):
    owned_items = Item.objects.filter(owner__id=request.user.id)
    owned_items=[item_serializer(item) for item in owned_items]
    return(success(owned_items, 'data'))


def sell_item(request):
    body=json.loads(request.body)
    item=Item.objects.get(id=body['item_id'])
    sell_type=body['sell_type']
    try:
        if(sell_type=='increment'):
            print("increment")
            sell=SellItemIncrement(item=item,starting=int(body['starting_price']),state='active',instant_sell=int(body['instant_sell']))
        elif(sell_type=='decrement'):
            print("decrement")
            sell=SellItemDecrement(item=item,starting=int(body['starting_price']),current_price=int(body['starting_price']),state='active',period=int(body['period']),stop_decrement=int(body['stop_decrement']),delta=int(body['delta']))
        elif(sell_type=='instant-increment'):
            print("instant-increment")
            sell=SellItemInstantIncrement(item=item,starting=int(body['starting_price']),current_price=int(body['instant_sell']),state='active', minbid=int(body['starting_price']))
        sell.save()
        sell.start_auction()
    except Exception as e:
        print(e)
        messages.add_message(request,messages.ERROR,message='Item is already in auction.')
    return(success({}, 'data'))


def sell_history(request):
    pass


def register_to_watch_item_type(request,type):
    try:
        #body=json.loads(request.body)
        WatchItemTypes.objects.create(user=request.user.userprofile, item_type=type)
        return(success({}, 'data'))
    except Exception as e:
        return(error(str(e))) 


def messages(request):
    try:
        messages=Messages.objects.all().filter(user=request.user.userprofile)
        messages=[x.message for x in messages]
        return(success(messages, 'data'))
    except Exception as e:
        return(error(str(e))) 


#this function not necessary for phase4 but to test phase3 it is neeeded
def bid_screen(request,item_id):
    if request.method=='GET':
        item=Item.objects.filter(id=item_id).first()
        print(item)
        context={
            'item':item
        }
        return render(request,'bid/bid_screen.html',context)
    else:
        body=json.loads(request.body)
        amount=int(body['amount'])
        user=User.objects.all().filter(id=request.user.id).select_related('userprofile').first().userprofile
        item=int(body['item_id'])
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