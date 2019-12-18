from django.shortcuts import render
from .models import Item
# Create your views here.
def home(request):
    items=Item.objects.all()
    context={
        'items':items
    }
    return render(request,'bid/home.html',context)

def bid_screen(request):
    return render(request,'bid/bid_screen.html')