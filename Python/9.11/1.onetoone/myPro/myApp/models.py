from django.db import models

# Create your models here.
class People(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField(null=True)
    sex = models.NullBooleanField(null=True,default=True)

class Card(models.Model):
    # int 正负 21亿  Integer
    code = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    person = models.OneToOneField(People, on_delete=models.CASCADE, primary_key=True)
