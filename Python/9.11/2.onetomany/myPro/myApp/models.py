from django.db import models

# Create your models here.

class People(models.Model):
    name = models.CharField(max_length=50)
    car_num = models.IntegerField(default=0)

    class Meta:
        db_table = 'people'

class Card(models.Model):
    number = models.CharField(max_length=20)
    person = models.ForeignKey(People,on_delete=models.CASCADE)
    source = models.CharField(max_length=50)

    class Meta:
        db_table = 'Card'