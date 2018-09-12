from django.db import models

# Create your models here.

class People(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    class Meta:
        db_table = 'people'
class Games(models.Model):
    gname = models.CharField(max_length=50)
    gtype = models.CharField(max_length=50)
    bind = models.ForeignKey(People,on_delete=models.CASCADE)
    class Meta:
        db_table = 'games'