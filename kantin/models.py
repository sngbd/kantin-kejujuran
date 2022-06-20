from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Item(models.Model):
    name = models.CharField(max_length=100, default=None)
    description = models.TextField()
    price = models.PositiveIntegerField(default=None)
    image = models.CharField(max_length=500)
    lister = models.CharField(max_length=100)
    datetime = models.CharField(max_length=64)


class Balance(models.Model):
    balance = models.PositiveIntegerField(default=0)
