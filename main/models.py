import uuid
from django.db import models
from django.contrib.auth.models import auth
from accounts.models import User
# Create your models here.


#---------------------------------------------------#

class group(models.Model):
    group_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    admin = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    members = models.ManyToManyField(User, 
                                        through='group_member', 
                                        through_fields=('group_id', 'user_id'),
                                        related_name='GroupMember',
                                    )
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    hash = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.name}'


class group_member(models.Model):
    group_id = models.ForeignKey(group, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

#---------------------------------------------------#

class service(models.Model):
    service_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    #service_type_id = models.ForeignKey()
    initiator_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    service_desc = models.TextField()
    start_time = models.DateTimeField(null=True)
    slackness = models.TimeField()
    members = models.ManyToManyField(User,
                                        through='service_member',
                                        through_fields=('service_id', 'user_id'),
                                        related_name='ServiceMember'
                                        )
    groups = models.ManyToManyField(group,
                                        through='service_group',
                                        through_fields=('service_id', 'group_id'),
                                        related_name='group_of_service',
                                        )

    def __str__(self):
        return self.service_desc

class shoping(service):
    pass

class food(service):
    pass

class travel(service):
    pass

class event(service):
    pass

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
    service_id = models.ForeignKey(service, on_delete=models.CASCADE)
    group_id = models.ForeignKey(group, on_delete=models.CASCADE)

class service_member(models.Model):
    service_id = models.ForeignKey(service, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

#---------------------------------------------------#
