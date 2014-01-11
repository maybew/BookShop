from django.db import models
from django.contrib.localflavor.us.models import USStateField
from conf.static import ORDER_STATUS
from item.models import Item

class Account(models.Model):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=30)    
    password = models.CharField(max_length=100)
    address = models.CharField(max_length=200, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    city = models.CharField(max_length=30, blank=True)
    state = USStateField(blank=True)
    zip = models.CharField(max_length=10, blank=True)
    
    def __unicode__(self):
        return self.email
    
class Order(models.Model):
    status = models.IntegerField(choices=ORDER_STATUS)
    account = models.ForeignKey(Account)
    item = models.ForeignKey(Item)
    quantity = models.IntegerField()
    time = models.DateTimeField(auto_now_add=True)
    price = models.FloatField()
    receive_name = models.CharField(max_length=30)
    receive_address = models.CharField(max_length=200)
    receive_city = models.CharField(max_length=30)
    receive_state = USStateField()
    receive_zip = models.CharField(max_length=10)
    bill_name = models.CharField(max_length=30)
    bill_address = models.CharField(max_length=200)
    bill_city = models.CharField(max_length=30)
    bill_state = USStateField()
    bill_zip = models.CharField(max_length=10)
    card_number = models.CharField(max_length=16)
    card_name = models.CharField(max_length=30)
    card_code = models.CharField(max_length=3)
    
    def __unicode__(self):
        return self.id