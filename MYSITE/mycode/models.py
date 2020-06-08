from django.db import models
from django.utils import timezone
import datetime

class newItem(models.Model):
    name_of_item = models.CharField(max_length=200)
    kind_of_item = models.CharField(max_length=200)
    price_of_item = models.CharField(max_length=200)
    pub_date = models.DateTimeField(max_length=200)
    # did not work in admin panel ofc
    #def __init__(self, name_of_item, kind_of_item, price_of_item):
        #self.name_of_item= name_of_item
        #self.kind_of_item= kind_of_item
        #self.price_of_item= price_of_item
        #self.pub_date= timezone.now()
    def __str__(self):
        return self.name_of_item
    #def year_of_pub(self):
    #    return pub_date
    #def timeOfAdd(self):
    #    return pub_date

# Create your models here.
