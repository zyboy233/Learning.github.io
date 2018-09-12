from django.db import models

# Create your models here.

class People(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
class Card(models.Model):
    code = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    person = models.OneToOneField(People,on_delete=models.CASCADE,primary_key=True)