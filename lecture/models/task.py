
from django.contrib.auth import get_user_model
from django.db import models
from .lecuture import Lecture


# Create your models here.
User = get_user_model()

class Task(models.Model):
   
    lecture = models.ForeignKey(Lecture,null=True ,blank=True, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    done = models.BooleanField()
    title = models.TextField()
    memo = models.TextField(null=True,blank=True)
    deadline = models.DateTimeField(null=True, blank=True)
    validAlarm =  models.BooleanField(null=True, blank=True)
    alarm = models.IntegerField(null=True, blank=True)
    url = models.URLField(null=True , blank=True)
    