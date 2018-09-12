from django.db import models

# Create your models here.
class Publication(models.Model):
    pname = models.CharField(max_length=200)
    paddress = models.CharField(max_length=200)
    class Meta:
        db_table = 'publication'
class Book(models.Model):
    bname = models.CharField(max_length=200)
    bauthor = models.CharField(max_length=200)
    publication = models.ManyToManyField(Publication)
    class Meta:
        db_table = 'book'