from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Item(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    owner=models.ForeignKey(User, on_delete=models.CASCADE)
    item_type=models.CharField(max_length=100)

class SellItem(models.Model):
    item=models.ForeignKey(Item, on_delete=models.CASCADE)
    starting=models.FloatField()
