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

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Restaurant(models.Model):
    name = models.CharField(null=False, max_length=1000)
    price = models.FloatField(null=True)
    cusine_category = models.CharField(null=True, max_length=500)
    city = models.CharField(null=True, max_length=100)
    region = models.CharField(null=True, max_length=100)
    url = models.URLField(null=True)
#    page_no = models.IntegerField(null=True)
    cusine_type = models.CharField(null=True, max_length=100)
    timing = models.CharField(null=True, max_length=100)
#    rating = models.CharField(null=True, max_length=100)
#    votes = models.CharField(null=True, max_length=100)

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(null=False, max_length=1000)
    domain = models.CharField(max_length=100)
    logo = models.URLField(null=True)
    timestamp = models.DateTimeField(null=True)

    def __str__(self):
        return self.name


class Location(models.Model):
    latitude = models.DecimalField(null=False, max_digits=10, decimal_places=7)
    longitude = models.DecimalField(null=False, max_digits=10, decimal_places=7)
    address = models.CharField(default='', max_length=1000)
    timestamp = models.DateTimeField(null=False)

    def __str__(self):
        return self.address

class service(models.Model):
    service_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    service_type_id = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    initiator_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    service_desc = models.TextField()
    start_time = models.DateTimeField(null=True)
    end_time=models.DateTimeField(null=True)
    slackness = models.TimeField()
    is_active=models.BooleanField(default=True)
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

class service_group(models.Model):
    service_id = models.ForeignKey(service, on_delete=models.CASCADE)
    group_id = models.ForeignKey(group, on_delete=models.CASCADE)

class service_member(models.Model):
    service_id = models.ForeignKey(service, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

class ShopingService(service):
    vendor = models.ForeignKey(Company, on_delete=models.DO_NOTHING, null=False)

    def __str__(self):
        return '%s' % self.vendor

class FoodService(service):
    vendor = models.ForeignKey(Restaurant, on_delete=models.DO_NOTHING, null=False)

    def __str__(self):
        return '%s' % self.vendor

class TravelService(service):
    start_point = models.ForeignKey(Location, on_delete=models.DO_NOTHING, null=False, related_name='start_loc')
    end_point = models.ForeignKey(Location, on_delete=models.DO_NOTHING, null=False, related_name='end_loc')
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
    location = models.CharField(null=False, max_length=1000)
    event_type = models.CharField(max_length=10, choices=EVENT_CHOICES)

#---------------------------------------------------#



class Message(models.Model):
    service_id = models.ForeignKey(service, on_delete=models.CASCADE)
    user_id =  models.ForeignKey(User, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return self.content + " " + str(self.timestamp)

#---------------------------------------------------#



#---------------------------------------------------#
