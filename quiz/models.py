from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Post(models.Model):
    xyz = models.CharField(max_length=200)
    yzw = models.CharField(max_length=200)