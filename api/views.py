from main.models import service
from rest_framework import generics,mixins,permissions,authentication,filters
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


# Create your views here.

class servicefilterview(generics.ListAPIView):
	serializer_class       =ServiceSerializer
	authentication_classes =[BasicAuthentication]
	permission_classes     =[IsAuthenticated]
	lookup_field=['service_id']
	
	def get_queryset(self):
		
		Service=self.request.query_params.get('service',None)
		Start_time=self.request.query_params.get('start_time',None)
		End_time=self.request.query_params.get('end_time',None)
		Groups=self.request.query_params.get('groups',None)
		
		queryset=service.objects.filter(members=self.request.user)
		
		if Service:
			queryset=queryset.filter(service_type__name=Service)
		
		if Groups:
			Groups=''.join(Groups.split(' ')).split(',')
			queryset=queryset.filter(groups__group_id__in=Groups)
			queryset=queryset.distinct()
		
		if Start_time:
			queryset=queryset.filter(start_time__gte=Start_time)
		
		if End_time:
			queryset=queryset.filter(end_time__lte=End_time)
		
		queryset=queryset.distinct()
		return queryset

class searchview(generics.ListAPIView):
	serializer_class=ServiceSerializer
	authentication_classes =[BasicAuthentication]
	permission_classes     =[IsAuthenticated]
	filter_backends        = [filters.SearchFilter]
	search_fields          = ['^service_type__name','^initiator__username','^groups__name']
	look_up_field=['service_id']
	
	def get_queryset(self):
		
		Service=self.request.query_params.get('service',None)
		Start_time=self.request.query_params.get('start_time',None)
		End_time=self.request.query_params.get('end_time',None)
		Groups=self.request.query_params.get('groups',None)
		
		queryset=service.objects.filter(members=self.request.user)
		
		if Service:
			queryset=queryset.filter(service_type__name=Service)
		
		if Groups:
			Groups=''.join(Groups.split(' ')).split(',')
			queryset=queryset.filter(groups__group_id__in=Groups)
			queryset=queryset.distinct()
		
		if Start_time:
			queryset=queryset.filter(start_time__gte=Start_time)
		
		if End_time:
			queryset=queryset.filter(end_time__lte=End_time)
		
		queryset=queryset.distinct()
		return queryset
	
@api_view(['PUT'])
def add_service_member(request):
	service_id=request.query_params.get('service_id',None)
	Service=service.objects.get(pk=service_id)
	Service.members.add(request.user)

	return Response({'message':'You have been added to this service Successfully'})