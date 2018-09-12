from django.db import models

# Create your models here.

class Stu(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
class Clsroom(models.Model):
    space = models.CharField(max_length=20)
    code = models.ManyToManyField(Stu)
