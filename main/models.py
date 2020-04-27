from django.db import models

# Create your models here.

#---------------------------------------------------#

class service(models.Model):
    group_id = models.ForeignKey(group, on_delete=models.CASCADE)
    service_type_id = models.ForeignKey()
    initiator_id =
    service_desc = TextField()
    start_time = models.DateTimeField()
    slackness = 

class shoping(service):

class food(service):

class travel(service):

class event(service):

#---------------------------------------------------#

class group(models.Model):

class group_member(models.Model):
    room = models.ManyToManyField(group)

#---------------------------------------------------#

class Message(models.Model):
    service_id = models.ForeignKey(service, on_delete=models.CASCADE)
    user_id =  models.ForeignKey()
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return self.content + " " + str(self.timestamp)

#---------------------------------------------------#

class service_group(models.Model):
