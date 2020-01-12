from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import UserRegisterForm 
from .models import UserProfile
from bid.views import Item
from bid.models import SellItemIncrement,SellItemDecrement, SellItemInstantIncrement
from online_bidding.serializers import *
from django.views.decorators.csrf import ensure_csrf_cookie
import json

from django.http import HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.conf import settings
from django.contrib.auth import login
from .tokens import account_activation_token
from django.contrib.auth.decorators import login_required
# Create your views here.
@ensure_csrf_cookie
def set_csrf(request):
    return 

@login_required
def index(request):
    return render(request, "build/index.html")

def register(request):
    if request.method== 'POST': 
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False) # hash password and save it to db
            username = form.cleaned_data['username']
            user.email = form.cleaned_data['email']
            user.set_password(form.cleaned_data['password1'])
            user.is_active = False
            # Save the User object
            user.save()

            current_site = get_current_site(request)
            subject = 'Activate your Account'
            message = render_to_string('users/account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            # send activation link to the user
            user.email_user(subject=subject, message=message)
            return HttpResponse('Please check your mail for activation')

            # messages.success(request, 'Account created for {}'.format(username))
            # return redirect('login')
    else:
        form=UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError,User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect('login')
    else:
        return render(request, 'users/account_activation_invalid.html')


def user_profile(request):
    user=User.objects.all().filter(id=request.user.id).select_related('userprofile').first().userprofile
    print(user_profile_serializer(user))
    return(success(user_profile_serializer(user), 'data'))

@login_required
def home(request):
    context = {
        'username': request.user.username 
    }
    return render(request,'users/home.html', context)


def list_items(request):
    if request.method=='GET':
        owned_items = Item.objects.filter(owner__id=request.user.id)
        print(owned_items)
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
                sell=SellItemDecrement(item=item,starting=int(request.POST['starting_price']),current_price=int(request.POST['starting_price']),state='active',period=int(request.POST['period']),stop_decrement=int(request.POST['stop_decrement']),delta=int(request.POST['delta']))
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
        body=json.loads(request.body)
        print(body)
        title=body['title']
        description=body['description']
        item_type=body['item_type']
        item = Item(title=title, description=description, owner=request.user.userprofile, item_type=item_type)
        item.save()
        return redirect('users_app:list_items')

def add_balance(request):
    body = json.loads(request.body)
    print('add balance body',body)
    amount = int(body['amount'])
    userprofile = User.objects.filter(id=request.user.id).select_related('userprofile').first().userprofile
    res = userprofile.add_balance(amount)
    if res:
        return success(user_profile_serializer(userprofile), 'data')
    else:
        return error('Could not update balance')

def change_password(request):
    body = json.loads(request.body)
    print('change password body',body)
    old_password = body['old_password']
    new_password = body['new_password']
    userprofile = User.objects.filter(id=request.user.id).select_related('userprofile').first().userprofile
    res = userprofile.change_password(old_password, new_password)
    if res:
        return success({}, 'data')
    else:
        return error('')