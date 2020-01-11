from django.urls import path
from . import views

app_name = 'bid_app'
urlpatterns=[
    path('',views.home,name='bid-home'),
    path('bidding/<int:item_id>',views.bid_screen,name='bid-bid-screen'),
    path('messages/',views.messages,name='bid-messages'),
    path('test/',views.test,name='bid-test'),
    path('list-items/',views.list_items,name='bid-list-items'),
    path('sell/',views.sell_item,name='bid-sell'),
    path('watch-item-type/<str:type>',views.register_to_watch_item_type,name='watch-item-type')
]
