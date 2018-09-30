from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib import admin
# Create your models here.

class UserModel(AbstractUser):
    account = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    version = models.IntegerField(default=0,verbose_name='版本')

@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username',)
    pass