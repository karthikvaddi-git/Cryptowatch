from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#model that stores all api data at regular intervals

class Cryptodata(models.Model):
    name = models.CharField(max_length=200)
    image = models.URLField()
    price = models.CharField(max_length=200)
    rank = models.CharField(max_length=10)
    market_cap = models.CharField(max_length=200)

    def __str__(self):
        return str(self.name)


#model to track trigger price of coin
class Cointracker(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=200)
    triggerprice=models.CharField(max_length=200)
    pricerises=models.BooleanField(default=True)
    messagesent=models.BooleanField(default=False)


    def __str__(self):
        return str(self.name)


class Phonenumber(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.IntegerField(unique=True)

    def __str__(self):
        return str(self.phone_number)











