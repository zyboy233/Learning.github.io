from django.db import models

# Create your models here.
class Goods(models.Model):
    name = models.CharField(max_length=100)
    des = models.CharField(max_length=1000)
    class Meta:
        db_table = 'goods'