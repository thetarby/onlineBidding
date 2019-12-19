from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import UserRegisterForm 
from .models import UserProfile
# Create your views here.
def register(request):
    if request.method== 'POST': 
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save() # hash password and save it to db
            username = form.cleaned_data['username']
            messages.success(request, 'Account created for {}'.format(username))
            return redirect('bid-home')
    else:
        form=UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})


def user_profile(request):
    print(User.objects.all().filter(id=request.user.id).select_related('userprofile').first())
    user=User.objects.all().filter(id=request.user.id).select_related('userprofile').first().userprofile
    return render(request, 'users/user_profile.html', {'user':user})

def home(request):
    context = {
        'username': request.user.username  # bu olmuyor ya gozukmuyor home pagede
    }
    return render(request,'users/home.html', context)


def list_items(request):
    return render(request,'users/list_items.html')


def add_item(request):
    return render(request,'users/add_item.html')