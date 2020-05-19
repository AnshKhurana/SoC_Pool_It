from rest_framework import serializers
from main.models import service

class serviceserializer(serializers.ModelSerializer):

	class Meta:
		model  =service
		exclude=['members','groups']

	
