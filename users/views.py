from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import UserRegisterForm 
from .models import UserProfile
from bid.views import Item
from bid.models import SellItemIncrement,SellItemDecrement, SellItemInstantIncrement

# Create your views here.
def register(request):
    if request.method== 'POST': 
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save() # hash password and save it to db
            username = form.cleaned_data['username']
            messages.success(request, 'Account created for {}'.format(username))
            return redirect('login')
    else:
        form=UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})


def user_profile(request):
    print(User.objects.all().filter(id=request.user.id).select_related('userprofile').first())
    user=User.objects.all().filter(id=request.user.id).select_related('userprofile').first().userprofile
    return render(request, 'users/user_profile.html', {'user':user})

def home(request):
    context = {
        'username': request.user.username 
    }
    return render(request,'users/home.html', context)


def list_items(request):
    if request.method=='GET':
        owned_items = Item.objects.filter(owner__id=request.user.id)
        context = {
            'owned_items': owned_items
        }
        return render(request,'users/list_items.html', context)
    if request.method=='POST':
        item=Item.objects.get(id=request.POST['item_id'])
        sell_type=request.POST['sell_type']
        try:
            if(sell_type=='increment'):
                print("increment")
                sell=SellItemIncrement(item=item,starting=int(request.POST['starting_price']),state='active',instant_sell=int(request.POST['instant_sell']))
            elif(sell_type=='decrement'):
                print("decrement")
                sell=SellItemDecrement(item=item,starting=0,current_price=100,state='active',period=10,stop_decrement=10,delta=10)
            elif(sell_type=='instant-increment'):
                print("instant-increment")
                sell=SellItemInstantIncrement(item=item,starting=int(request.POST['starting_price']),current_price=int(request.POST['instant_sell']),state='active', minbid=int(request.POST['starting_price']))
            sell.save()
            sell.start_auction()
        except Exception as e:
            print(e)
            messages.add_message(request,messages.ERROR,message='Item is already in auction.')
        owned_items = Item.objects.filter(owner__id=request.user.id)
        print(owned_items)
        context = {
            'owned_items': owned_items
        }
        return render(request,'users/list_items.html', context)


def add_item(request):
    if request.method=='GET':
        return render(request,'users/add_item.html')
    else:
        title=request.POST['title']
        description=request.POST['description']
        item_type=request.POST['item_type']
        item = Item(title=title, description=description, owner=request.user, item_type=item_type)
        item.save()
        return redirect('users_app:list_items')
