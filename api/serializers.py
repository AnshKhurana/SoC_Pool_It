from rest_framework import serializers
from main.models import *
from accounts.models import User
from typing import Dict


class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model=User
		fields=['username']


class CategorySerializer(serializers.ModelSerializer):

	class Meta:
		model=Category
		fields=['name']




class PolymorphicSerializer(serializers.Serializer):
	
	def get_serializer_map(self) -> Dict[str, serializers.Serializer]:
		'''return the dictionary mapping keys to serializers'''
		raise NotImplementedError

	def to_representation(self, obj):
		
		type_str = obj.service_type.name
		try:
			serializer = self.get_serializer_map()[type_str]
		except KeyError:
			raise ValueError(
				'Serializer for "{}" does not exist'.format(type_str),
			)

		data = serializer(obj, context=self.context).to_representation(obj)
		user=obj.members.get(username=data['initiator']['username'])
		if user:
			data['is_member']=True
		else:
			data['is_member']=False
		return data

	def to_internal_value(self, data):

		try:
			serializer = self.get_serializer_map()[data['service_type']['name']]
		except KeyError:
			raise serializers.ValidationError({
				'service_type': 'Serializer for "{}" does not exist'.format(type_str),
			})

		validated_data = serializer(context=self.context).to_internal_value(data)
		return validated_data

	'''def create(self, validated_data):
		"""
		Translate validated data representation to object
		Override to allow polymorphism
		"""
		serializer = self.get_serializer_map()[validated_data['type']]
		return serializer(context=self.context).create(validated_data)'''

	'''def update(self,instance,validated_data):
		serializer=self.get_serializer_map()[validated_data['service_type']['name']]
		validated_data.pop('is_member')
		return serializer(context=self.context).update(instance, validated_data)'''



class ServiceSerializer(serializers.ModelSerializer):

	is_member=serializers.BooleanField()

	class Meta:
		model=service
		exclude=['groups','polymorphic_ctype',]
		read_only_fields=['initiator','service_type','start_time']


	def get_serializer_map(self) -> Dict[str, serializers.Serializer]:
		"""
		Return serializer map
		"""
		return {
			str('Food'): FoodServiceSerializer,
			str('Event'): EventServiceSerializer,
			str('Shopping'): ShoppingServiceSerializer,
			str('Travel'): TravelServiceSerializer,
			str('Other'): OtherServiceSerializer,
		}


	def to_representation(self, obj):
		
		type_str = obj.service_type.name
		try:
			serializer = self.get_serializer_map()[type_str]
		except KeyError:
			raise ValueError(
				'Serializer for "{}" does not exist'.format(type_str),
			)

		data = serializer(obj, context=self.context).to_representation(obj)
#		data['initiator']=data['initiator']['username']
		user=obj.members.get(username=data['initiator']['username'])
		if user:
			data['is_member']=True
		else:
			data['is_member']=False
		return data

	def to_internal_value(self, data):

		try:
			serializer = self.get_serializer_map()[data['service_type']['name']]
		except KeyError:
			raise serializers.ValidationError({
				'service_type': 'Serializer for "{}" does not exist'.format(type_str),
			})

		validated_data = serializer(context=self.context).to_internal_value(data)
		return validated_data

class FoodServiceSerializer(serializers.ModelSerializer):
	initiator=UserSerializer(allow_null=False)
	service_type=CategorySerializer(allow_null=False)

	class Meta:
		model=FoodService
		exclude=['groups','members','polymorphic_ctype',]
		read_only_fields=['initiator','service_type','start_time','vendor']



class ShoppingServiceSerializer(serializers.ModelSerializer):
	initiator=UserSerializer(allow_null=False)
	service_type=CategorySerializer(allow_null=False)

	class Meta:
		model=ShoppingService
		exclude=['groups','members','polymorphic_ctype',]
		read_only_fields=['initiator','service_type','start_time','vendor']

class EventServiceSerializer(serializers.ModelSerializer):
	initiator=UserSerializer(allow_null=False)
	service_type=CategorySerializer(allow_null=False)

	class Meta:
		model=EventService
		exclude=['groups','members','polymorphic_ctype',]
		read_only_fields=['initiator','service_type','start_time','location','event_type']

class TravelServiceSerializer(serializers.ModelSerializer):
	initiator=UserSerializer(allow_null=False)
	service_type=CategorySerializer(allow_null=False)

	class Meta:
		model=TravelService
		exclude=['groups','members','polymorphic_ctype',]
		read_only_fields=['initiator','service_type','start_time','start_point','end_point','transport']
class OtherServiceSerializer(serializers.ModelSerializer):
	initiator=UserSerializer(allow_null=False)
	service_type=CategorySerializer(allow_null=False)

	class Meta:
		model=OtherService
		exclude=['groups','members','polymorphic_ctype',]
		read_only_fields=['initiator','service_type','start_time']

