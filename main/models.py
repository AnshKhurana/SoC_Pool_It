import uuid
from django.db import models
from django.contrib.auth.models import auth
from django.conf import settings
from polymorphic.models import PolymorphicModel
from accounts.models import User
# Create your models here.

#---------------------------------------------------#

class group(models.Model):
    group_id = models.UUIDField(primary_key=True,unique=True, default=uuid.uuid4, editable=False)
    admin = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, 
                                        through='group_member', 
                                        through_fields=('group_id', 'user_id'),
                                        related_name='joined_groups',
                                    )
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1000)
    hash = models.CharField(max_length=64,unique=True, default=None)

    def __str__(self):
        return f'{self.name}'


class group_member(models.Model):
    group_id = models.ForeignKey(group, on_delete=models.CASCADE)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

#---------------------------------------------------#

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class service(PolymorphicModel):
    service_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    service_type = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    initiator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    service_desc = models.CharField(max_length=1000,null=False)
    start_time = models.DateTimeField(null=True)
    end_time=models.DateTimeField(null=True)
    is_active=models.BooleanField(default=True)
    members = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                        through='service_member',
                                        through_fields=('service', 'user'),
                                        related_name='ServiceMember'
                                        )
    groups = models.ManyToManyField(group,
                                        through='service_group',
                                        through_fields=('service', 'group'),
                                        related_name='group_of_service',
                                        )

    def __str__(self):
        return self.service_desc


class ShoppingService(service):
    vendor = models.CharField(max_length=1000)

    def __str__(self):
        return '%s' % self.vendor

class FoodService(service):
    vendor = models.CharField(max_length=1000)

    def __str__(self):
        return '%s' % self.vendor

class TravelService(service):
    start_point = models.CharField(max_length=1000, null=False)
    end_point = models.CharField(max_length=1000, null=False)
    TRAVEL_CHOICES = [
        ('Taxi', 'Taxi'),
        ('Train', 'Train'),
        ('Flight', 'Flight'),
    ]
    transport = models.CharField(max_length=10, choices=TRAVEL_CHOICES, null=True)

    def __str__(self):
        return '%s' % self.transport

class EventService(service):
    EVENT_CHOICES = [
        ('Movie', 'Movie'),
        ('Concert', 'Concert'),
    ]
    location = models.CharField(max_length=1000,null=False)
    event_type = models.CharField(max_length=10, choices=EVENT_CHOICES)

class OtherService(service):
    pass



class Message(models.Model):
    service = models.ForeignKey(service,related_name = 'MessageService' ,on_delete=models.CASCADE,)
    user =  models.ForeignKey(settings.AUTH_USER_MODEL,related_name = 'UserMessage', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    seen = models.ManyToManyField(settings.AUTH_USER_MODEL,related_name = 'seenby')
    def __str__(self):
        return self.content + " " + str(self.timestamp)

class service_group(models.Model):
    service = models.ForeignKey(service, on_delete=models.CASCADE)
    group = models.ForeignKey(group, on_delete=models.CASCADE)


class service_member(models.Model):
    service = models.ForeignKey(service, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

#---------------------------------------------------