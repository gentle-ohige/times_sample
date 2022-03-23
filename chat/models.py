from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()
# class Contact(models.Model):
#     user = models.ForeignKey(
#         User, related_name='friends', on_delete=models.CASCADE)
#     friends = models.ManyToManyField('self', blank=True)

#     def __str__(self):
#         return self.user.username


class Message(models.Model):

    content = models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return ''


class Chat(models.Model):

    room = models.CharField(max_length=200, default='')
    participants = models.ManyToManyField(User, blank=True)
    messages = models.ManyToManyField(Message, blank=True)
    # update = models.DateTimeField(auto_now_add=True)
    # createAt = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return "{}".format(self.pk)