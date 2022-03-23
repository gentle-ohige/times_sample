from datetime import datetime
from util.storage import OverwriteStorage
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone
from firebase_admin.auth import get_user

from django.contrib.auth.models import User

class UserProfile(models.Model):
    
    def iconUploadPath(instance, filename):
        return 'user/{0}/profile/{1}'.format(instance.id, filename)


    room = models.CharField(max_length=200, blank=True, default="")
    icon = models.CharField(max_length=200, blank=True, default="")
    iconImage = models.ImageField(upload_to=iconUploadPath, storage=OverwriteStorage(),  blank=True)
    display_name = models.CharField(max_length=200, blank=True, default="")
    update_date = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    list_display = ('icon', 'iconImage', 'display_name')
    

        

class UserIcon(models.Model):
    iconImage = models.ImageField(upload_to ='media/', blank=True)
    list_display = ('iconImage')
    