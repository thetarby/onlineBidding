from django.urls import path
from . import views

app_name = 'bid_app'
urlpatterns=[
    path('',views.home,name='bid-home'),
    path('bidding/<int:item_id>',views.bid_screen,name='bid-bid-screen'),
    path('messages/',views.messages,name='bid-messages'),
    path('test/',views.test,name='bid-test')
]
