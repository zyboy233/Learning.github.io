from django.db import models

# Create your models here.

class People(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    code = models.CharField(max_length=20,primary_key=True)
class Card(models.Model):
    card_code = models.OneToOneField(People,on_delete=True,primary_key=True)
    card_type = models.CharField(max_length=20)