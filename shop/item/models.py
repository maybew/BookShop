from django.db import models
from conf.static import ITEM_STATUS

class Category(models.Model):
    name = models.CharField(max_length=30)
    
    def __unicode__(self):
        return self.name
    
class Item(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=30)
    category = models.ForeignKey(Category)
    price = models.FloatField()
    description = models.CharField(max_length=300)
    status = models.IntegerField(choices=ITEM_STATUS)
    inventory = models.IntegerField()
    weight = models.FloatField()
    image = models.ImageField(upload_to='images')
    time = models.DateTimeField(auto_now_add=True)
    
    def __unicode__(self):
        return self.title
