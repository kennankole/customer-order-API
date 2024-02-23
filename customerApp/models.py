from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Customer(AbstractUser):
  customer_code = models.CharField(max_length=5)
  phone_number = models.CharField(max_length=13, default="+254XXXXXXXXX")

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

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
  if created:
    Token.objects.create(user=instance)
    

