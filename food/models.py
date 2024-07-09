from django.db import models
from django.contrib.auth.models import User

class Starters(models.Model):
    name=models.CharField(max_length=120)
    price=models.DecimalField(max_digits=4,decimal_places=2)
    simg=models.URLField()

class main_course(models.Model):
    name=models.CharField(max_length=120)
    price=models.DecimalField(max_digits=6,decimal_places=2)
    Mimg=models.URLField()

class desserts(models.Model):
    name=models.CharField(max_length=120)
    price=models.DecimalField(max_digits=5,decimal_places=2)
    Dimg=models.URLField()



