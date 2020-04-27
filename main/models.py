import uuid
from django.db import models
from django.contrib.auth.models import User, auth

# Create your models here.

#---------------------------------------------------#

class service(models.Model):
    service_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    group_id = models.ForeignKey(group, on_delete=models.CASCADE)
    service_type_id = models.ForeignKey()
    initiator_id = models.ForeignKey(User)
    service_desc = TextField()
    start_time = models.DateTimeField()
    slackness = models.TimeField()

class shoping(service):

class food(service):

class travel(service):

class event(service):

#---------------------------------------------------#

class group(models.Model):
    group_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

class group_member(models.Model):
    room = models.ManyToManyField(group)
    group_id = models.ForeignKey(group, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

#---------------------------------------------------#

class Message(models.Model):
    service_id = models.ForeignKey(service, on_delete=models.CASCADE)
    user_id =  models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return self.content + " " + str(self.timestamp)

#---------------------------------------------------#

class service_group(models.Model):
