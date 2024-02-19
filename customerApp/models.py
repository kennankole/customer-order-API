from typing import Iterable
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Customer(AbstractUser):
  code = models.CharField(max_length=5)

  class Meta:
    ordering = ['username']
    
  def save(self, *args, **kwargs) -> None:
    return super().save(*args, **kwargs)

class Order(models.Model):
  item = models.CharField(max_length=250)
  amount = models.IntegerField()
  customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
  owner = models.ForeignKey(Customer, related_name="orders", on_delete=models.CASCADE, default=1)
  class Meta:
    ordering = ['item', 'amount']
    
  def save(self, *args, **kwargs):
    return super().save(*args, **kwargs)