from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    mobile = models.IntegerField(default=False)
    address = models.CharField(max_length=100)