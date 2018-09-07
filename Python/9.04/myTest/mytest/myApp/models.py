from django.db import models

# Create your models here.

class Table1(models.Model):
    name = models.CharField(max_length=20,unique=True)
    age = models.IntegerField()

    def __str__(self):
        return self.name+','+self.age
