from django.db import models
from django.conf import settings
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    birth_date = models.DateField(null=True,blank=True)
    photo = models.ImageField(upload_to='user/%Y/%m/%d',blank=True)

    def __str__(self):
        return '{} profile'.format(self.user.username)
