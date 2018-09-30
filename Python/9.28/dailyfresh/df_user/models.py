# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class UserInfo(models.Model):
    u_name = models.CharField(max_length=20)
    u_password = models.CharField(max_length=200)
    u_email = models.CharField(max_length=60)
    u_shou_address = models.CharField(max_length=200)
    u_postcode = models.CharField(max_length=6)
    u_phone = models.CharField(max_length=11)

