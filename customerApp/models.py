from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Customer(AbstractUser):
  code = models.CharField(max_length=5)

  class Meta:
    ordering = ['username']