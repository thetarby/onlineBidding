from django.urls import path
from . import views

app_name = 'users_app'
urlpatterns=[
    path('',views.home,name='home'),
    path('list_items/',views.list_items,name='list_items'),
    path('add_item/',views.add_item,name='add_item'),
    path('deneme/',views.set_csrf,name='asda'),
    path('index/',views.index,name='index'),
    path('activate/<slug:uidb64>/<slug:token>)/', views.activate, name='activate'),
    path('add_balance/',views.add_balance,name='add_balance'),
    path('change_password/',views.change_password,name='change_password'),
]