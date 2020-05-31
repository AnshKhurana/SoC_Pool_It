from main.models import service,FoodService,EventService,TravelService,ShoppingService
from django.db.models import Q
from django.utils import timezone
from .serializers import *
from rest_framework import generics,mixins,permissions,authentication,filters
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated



# Create your views here.

class servicefilterview(generics.ListAPIView):
	serializer_class=ServiceSerializer
	
	def get_queryset(self):
		
		Service=self.request.GET.get('service',None)
		Start_time=self.request.GET.get('start_time',None)
		End_time=self.request.GET.get('end_time',None)
		Groups=self.request.GET.get('group_ids',None)
		Text=self.request.GET.get('text',None)
		filt=Q(groups__members=self.request.user)&Q(is_active=True)
		
		if Service :
			if Service!='All':
				filt=filt&Q(service_type__name=Service)

		if Groups:
			Groups=''.join(Groups.split(' ')).split(',')
			filt=filt&Q(groups__group_id__in=Groups)
		
		if Start_time:
			filt=filt&Q(start_time__gte=Start_time)

		if End_time:
			filt=filt&Q(end_time__lte=End_time)


		if Text:

			if Service=='Food':
				queryset=FoodService.objects.filter(filt&Q(service_desc__icontains=Text)|\
					Q(initiator__username__icontains=Text)|Q(vendor__icontains=Text)).distinct().all()
				
			elif Service=='Shopping':
				queryset=ShoppingService.objects.filter(filt&Q(service_desc__icontains=Text)|\
					Q(initiator__username__icontains=Text)|Q(vendor__icontains=Text)).distinct().all()

			elif Service=='Event':
				queryset=EventService.objects.filter(filt&Q(service_desc__icontains=Text)|\
					Q(initiator__username__icontains=Text)|Q(location__icontains=Text)|Q(event_type__icontains=Text)).distinct().all()
			
			elif Service=='Travel':
				queryset=TravelService.objects.filter(filt&Q(service_desc__icontains=Text)|Q(initiator__username__icontains=Text)|\
					Q(transport__icontains=Text)|Q(start_point__icontains=Text)|Q(end_point__icontains=Text)).distinct().all()
		
			else:
				queryset=service.objects.filter(filt&Q(service_desc__icontains=Text)|Q(initiator__username__icontains=Text)).distinct().all()

		else:
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
		Service.is_active=False
		print(Service.is_active)
		Service.save()
		return Response({'message':'Service has Ended'})
