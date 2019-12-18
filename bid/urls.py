from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='bid-home'),
    path('bidding/',views.bid_screen,name='bid-bid-screen'),
]