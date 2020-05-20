from rest_framework import serializers
from main.models import *

class ServiceSerializer(serializers.ModelSerializer):

	class Meta:
		model=service
		fields='__all__'

#	read_only_fields=['service_type','service_desc','initiator','start_time','end_time','is_active','groups']
	

class FoodServiceSerializer(serializers.ModelSerializer):

	class Meta:
		model=FoodService
		fields='__all__'
		

#	read_only_fields=['service_type','service_desc','initiator','start_time','end_time','is_active','groups']

class TravelServiceSerializer(serializers.ModelSerializer):

	class Meta:
		model=TravelService
		fields='__all__'


class EventServiceSerializer(serializers.ModelSerializer):
	class Meta:
		model=EventService
		fields='__all__'
	

class ShoppingServiceSerializer(serializers.ModelSerializer):
	class Meta:
		model=ShoppingService
		fields='__all__'

