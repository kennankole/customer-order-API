from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Customer(AbstractUser):
  code = models.CharField(max_length=5)

  class Meta:
    ordering = ['username']
    

class Order(models.Model):
  item = models.CharField(max_length=250)
  amount = models.IntegerField()
  customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
  
  class Meta:
    ordering = ['item', 'amount']