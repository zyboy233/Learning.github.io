from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class MyUser(AbstractUser):
    age = models.CharField(max_length=100)
    fond = models.CharField(max_length=200)
    class Meta:
        db_table = 'my_user'