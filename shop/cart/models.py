from django.db import models
from account.models import Account
from item.models import Item
from conf.static import PROMOTION_TYPE

class Promotion(models.Model):
    code = models.CharField(max_length=20)
    type = models.IntegerField(choices=PROMOTION_TYPE)
    amount = models.DecimalField(max_digits=100, decimal_places=2)
    item = models.ForeignKey(Item, blank=True)
    expire_date = models.DateTimeField()
    
    def __unicode__(self):
        return self.code

class Cart(models.Model):
    account = models.OneToOneField(Account)
    promotion = models.ManyToManyField(Promotion, blank=True)
    
class CartItem(models.Model):
    cart = models.ForeignKey(Cart)
    item = models.ForeignKey(Item)
    quantity = models.IntegerField()