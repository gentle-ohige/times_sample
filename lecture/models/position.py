from os import name
from django.db import models
from django.db.models.fields.related import ManyToManyField

class Position(models.Model):
    x =  models.IntegerField()
    y =  models.IntegerField()
    
