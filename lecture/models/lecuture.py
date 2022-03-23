from os import name
from re import T
from .position import Position
from .teacher import Teacher
from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()
class Lecture(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title =  models.TextField()
    positions = models.ManyToManyField(Position,blank=True)
    teachers = models.ManyToManyField(Teacher, blank=True)