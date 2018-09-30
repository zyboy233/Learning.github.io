from django.db import models

# Create your models here.

class Publisher(models.Model):
    pname = models.CharField(max_length=50,primary_key=True)
    paddress = models.CharField(max_length=100,null=True)
    class Meta:
        db_table = 'Publisher'
class Book(models.Model):
    bname = models.CharField(max_length=50)
    bid = models.ManyToManyField(Publisher)
    class Meta:
        db_table = 'Book'