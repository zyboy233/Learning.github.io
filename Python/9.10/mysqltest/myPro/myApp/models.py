from django.db import models

# Create your models here.

class Three(models.Model):
    user = models.TextField()
    age = models.TextField()
class Four(models.Model):
    u_id = models.OneToOneField(Three,on_delete=models.CASCADE,primary_key=True)
    des = models.TextField()
    font = models.TextField()
