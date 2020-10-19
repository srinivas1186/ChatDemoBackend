from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Room(models.Model):
    users = models.ManyToManyRel(to=User,field='id')

class Message(models.Model):
    room_id = models.ForeignKey(Room,on_delete=models.CASCADE)
    content = models.TextField(verbose_name="message data")
    createdAt = models.DateTimeField(editable=False)

    def save(self,*args,**kwargs):
        if not self.id:
            self.createdAt = timezone.now()