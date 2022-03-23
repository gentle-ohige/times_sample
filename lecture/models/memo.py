from os import name
from datetime import datetime
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.fields.related import ManyToManyField
from . import *
# Create your models here.
User = get_user_model()

class Memo(models.Model):
    lecture = models.ForeignKey(Lecture,null=True ,blank=True, on_delete=models.CASCADE)
    updatedAt = models.DateTimeField(auto_now_add=True)
    createdAt = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    
    def save(self, *args, **kwargs):
        self.updatedAt = datetime.now()
        super(Memo, self).save(*args, **kwargs)
        
