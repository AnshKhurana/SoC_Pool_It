from main.models import service
from django.db.models import Q,Case,When
from django.utils import timezone
from .serializers import *
from rest_framework import generics,mixins,permissions,authentication,filters
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated



# Create your views here.

class servicefilterview(generics.ListAPIView):
	serializer_class       =ServiceSerializer
#	authentication_classes =[BasicAuthentication]
#	permission_classes     =[IsAuthenticated]
	
	def get_queryset(self):
		
		Service=self.request.GET.get('service',None)
		print(Service)
		Start_time=self.request.GET.get('start_time',None)
		print(Start_time)
		End_time=self.request.GET.get('end_time',None)
		print(End_time)
		Groups=self.request.GET.get('group_ids',None)
		print(Groups)
		Text=self.request.GET.get('text',None)
		print(Text)
		filt=Q(groups__members=self.request.user)
		
		#queryset=service.objects.filter(members=self.request.user)
		
		if Service :
			if Service!='All':
				#queryset=queryset.filter(service_type__name__in=Services)
				filt=filt&Q(service_type__name=Service)

		if Groups:
			Groups=Groups.split(" ")
			#queryset=queryset.filter(groups__group_id__in=Groups).distinct()
			filt=filt&Q(groups__group_id__in=Groups)
		
		if Start_time:
			#queryset=queryset.filter(start_time__gte=Start_time)
			filt=filt&Q(start_time__gte=Start_time)

		if End_time:
			#queryset=queryset.filter(end_time__lte=End_time)
			filt=filt&Q(end_time__lte=End_time)

		if Text:

			if service in ['Food','Shopping']:
				filt=filt&(Q(service_desc__icontains=Text)|Q(initiator__username__icontains=Text)|Q(vendor__icontains=Text))
				
			else:
				filt=filt&(Q(service_desc__icontains=Text)|Q(initiator__username__icontains=Text))
		
		
		queryset=service.objects.filter(filt).distinct().all()
		
		return queryset


	def list(self,request):
		queryset=self.get_queryset()
		serializer=ServiceSerializer(queryset,many=True,context={'user':request.user})
		return Response(serializer.data)

	
@api_view(['GET'])
def add_service_member(request):
	service_id=request.GET.get('id',None)
	Service=service.objects.get(pk=service_id)
	if Service.end_time > timezone.now():
		Service.members.add(request.user)
		return Response({'message':'Successfully joined the service'})
	else:
		return Response({'message':'Service has Ended'})
