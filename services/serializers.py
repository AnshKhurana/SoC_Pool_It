from rest_framework import serializers
from main.models import *
from accounts.models import User


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model=User
		fields=['username']


class CategorySerializer(serializers.ModelSerializer):

	class Meta:
		model=Category
		fields=['name']



class ServiceSerializer(serializers.ModelSerializer):

	vendor=serializers.CharField(required=False,max_length=1000)
	start_point=serializers.CharField(required=False,max_length=1000,allow_null=False)
	end_point=serializers.CharField(required=False,max_length=1000,allow_null=False)
	TRAVEL_CHOICES = [
		('Taxi', 'Taxi'),
		('Train', 'Train'),
		('Flight', 'Flight'),
    ]
	transport = serializers.ChoiceField(required=False, choices=TRAVEL_CHOICES, allow_null=False)
	EVENT_CHOICES = [
		('Movie', 'Movie'),
		('Concert', 'Concert'),
    ]
	location = serializers.CharField(max_length=1000,required=False,allow_null=False)
	event_type = serializers.ChoiceField(required=False, choices=EVENT_CHOICES)
	initiator=UserSerializer()
	
	service_type=CategorySerializer()

	class Meta:
		model=EventService
		exclude=['groups']




