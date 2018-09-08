from django.db import models

# Create your models here.

class Data(models.Model):
    tid = models.AutoField(primary_key=True)
    sourse = models.CharField(max_length=200,null=True)
    title = models.CharField(max_length=300,null=True)
    link = models.CharField(max_length=500,null=True)
    category = models.CharField(max_length=100,null=True)
    ptime = models.CharField(max_length=100,null=True)
