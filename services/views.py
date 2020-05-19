from main.models import group,Category,service_group,service_member,service			
from services.forms import groupsform,FoodServiceForm,EventServiceForm,TravelServiceForm,ShoppingServiceForm,OtherServiceForm
from django.utils import timezone
from django.contrib import messages
from django.shortcuts import render,get_list_or_404,redirect
from rest_framework import generics,mixins,permissions,authentication
from rest_framework.response import Response
from .serializers import serviceserializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated


'''class MultipleFieldLookupMixin(object):

	def get_queryset(self):
		queryset=services.objects.filter(members=self.request.user)
		queryset=self.filter_queryset(queryset)
		filter={}
		for field in many_lookup_fields:
			if self.kwargs[field]:
				filter[field]=self.kwargs[field]
		obj_list=get_list_or_404(queryset,**filter)'''
		

'''class servicefilterview(generics.ListAPIView):

	serializer_class       = ['serviceserializer']
	permission_classes     = [IsAuthenticated]
	authentication_classes = [BasicAuthentication]
	 
	def get_queryset(self):
		user=self.request.user
		Service=self.kwargs['service']
		queryset=service.objects.filter(members=self.request.user).filter(service_type__name=Service)
		return queryset

	def list(self,request,**kwargs):
		queryset=self.get_queryset()
		serializer=serviceserializer(queryset,many=True)
		return Response(serializer.data)

class groupsfilterview(generics.ListAPIView):
	serializer_class       = ['serviceserializer']
	permission_classes     = [IsAuthenticated]
	authentication_classes = [BasicAuthentication]
	 
	def get_queryset(self):
		user=self.request.user
		Groups=self.kwargs['groups']
		queryset=service.objects.filter(members=self.request.user).filter(groups__group_id__in=Groups)
		return queryset

	def list(self,request,**kwargs):
		queryset=self.get_queryset()

		serializer=serviceserializer(queryset,many=True)
		return Response(serializer.data)

class timefilterview(generics.ListAPIView):

	serializer_class       = ['serviceserializer']
	permission_classes     = [IsAuthenticated]
	authentication_classes = [BasicAuthentication]
	 
	def get_queryset(self):
		user=self.request.user
		start_time=self.kwargs['start_time']
		end_time=self.kwargs['end_time']
		queryset=service.objects.filter(members=self.request.user).filter(service_type__name=Service)
		return queryset

	def list(self,request,**kwargs):
		queryset=self.get_queryset()
		serializer=serviceserializer(queryset,many=True)
		return Response(serializer.data)'''


class servicefilterview(generics.ListAPIView):

	serializer_class       =['serviceserializer']
	authentication_classes =[BasicAuthentication]
	permission_classes     =[IsAuthenticated]
	
	def get_queryset(self):
		
		Service=self.request.query_params.get('service',None)
		Start_time=self.request.query_params.get('start_time',None)
		End_time=self.request.query_params.get('end_time',None)
		Groups=self.request.query_params.get('groups',None)
		
		queryset=service.objects.filter(members=self.request.user)
		if Service:
			queryset=queryset.filter(service_type__name=Service)
		if Groups:
			queryset=queryset.filter(groups__name__in=Groups)
			queryset=queryset.distinct()
		if Start_time:
			queryset=queryset.filter(start_time__gte=Start_time)
		if End_time:
			queryset=queryset.filter(end_time__lte=End_time)
		return queryset

	def list(self,request,**kwargs):
		queryset=self.get_queryset()
		serializer=serviceserializer(queryset,many=True)
		return Response(serializer.data)



def servicegroups(request):
	
	if request.method=="POST":
		
		form=groupsform(request.POST,user=request.user)
		
		if form.is_valid():
			c=list(form.cleaned_data['groups_list'].values_list('group_id',flat=True))
			request.session['servicegroups']=[str(o) for o in c ]
			print(request.session['servicegroups'])

			if request.POST['category']=='Food':
				request.session['category']='Food'
				return render(request,'ServiceForm.html',{'form':FoodServiceForm(),'name':'Food'})
		
			elif request.POST['category']=='Event':
				request.session['category']='Event'
				return render(request,'ServiceForm.html',{'form':EventServiceForm(),'name':'Event'})

			elif request.POST['category']=='Shopping':
				request.session['category']='Shopping'
				return render(request,'ServiceForm.html',{'form':ShoppingServiceForm(),'name':'Shopping'})
		
			elif request.POST['category']=='Travel':
				request.session['category']='Travel'
				return render(request,'ServiceForm.html',{'form':TravelServiceForm(),'name':'Travel'})

			else:
				request.session['category']='Other'
				return render(request,'ServiceForm.html',{'form':OtherServiceForm(),'name':' '})

		else:
			return render(request,'servicegroups.html',{'form':form})

	else:
		if group.objects.filter(members=request.user):
			return render(request,'servicegroups.html',{'form':groupsform(user=request.user)})
		else:
			return render(request,'servicegroups.html',{'form':groupsform(user=request.user),\
				'error_message':'You must be present in atleast one group to create the service'})


def createservice(request):
	if request.method=='POST':
		if request.session['category']=='Food':
			form=FoodServiceForm(request.POST)
			if form.is_valid():
				Service=form.save(commit=False)
				Service.start_time=timezone.now()
				Service.service_type=Category.objects.get(name='Food')
				Service.initiator=request.user
				Service.save()
				groups_ids=request.session['servicegroups']
				Service.members.add(request.user)
				sm=service_member(service=Service,user=request.user)
				sm.save()
				print(Service.members)
				for ID in groups_ids:
					Group=group.objects.get(pk=ID)
					Service.groups.add(Group)
					print(Service.groups)
					sg=service_group(service=Service,group=Group)
					sg.save()
					
				messages.success(request,'Successfully created a Service')
				return redirect('/accounts/signin')
			else:
				return render(request,'ServiceForm.html',{'form':form,'name':'Food '})
		
		elif request.session['category']=='Event':
			form=EventServiceForm(request.POST)
			if form.is_valid():
				Service=form.save(commit=False)
				Service.start_time=timezone.now()
				Service.service_type=Category.objects.get(name='Event')
				Service.initiator=request.user
				Service.save()
				groups_ids=request.session['servicegroups']
				Service.members.add(request.user)
				sm=service_member(service=Service,user=request.user)
				sm.save()
				for id in groups_ids:
					Group=group.objects.get(pk=id)
					Service.groups.add(Group)
					sg=service_group(service=Service,group=Group)
					sg.save()
					
				messages.success(request,'Successfully created a Service')
				return redirect('/accounts/signin')
			else:
				return render(request,'ServiceForm.html',{'form':form,'name':'Event '})
		
		elif request.session['category']=='Shopping':
			form=ShoppingServiceForm(request.POST)
			if form.is_valid():
				Service=form.save(commit=False)
				Service.start_time=timezone.now()
				Service.service_type=Category.objects.get(name='Shopping')
				Service.initiator=request.user
				Service.save()
				groups_ids=request.session['servicegroups']
				Service.members.add(request.user)
				sm=service_member(service=Service,user=request.user)
				sm.save()
				for id in groups_ids:
					Group=group.objects.get(pk=id)
					Service.groups.add(Group)
					sg=service_group(service=Service,group=Group)
					sg.save()
					
				messages.success(request,'Successfully created a Service')
				return redirect('/accounts/signin')
			else:
				return render(request,'ServiceForm.html',{'form':form,'name':'Shopping '})
		
		elif request.session['category']=='Travel':
			form=TravelServiceForm(request.POST)
			if form.is_valid():
				Service=form.save(commit=False)
				Service.start_time=timezone.now()
				Service.service_type=Category.objects.get(name='Travel')
				Service.initiator=request.user
				Service.save()
				groups_ids=request.session['servicegroups']
				Service.members.add(request.user)
				sm=service_member(service=Service,user=request.user)
				sm.save()
				for id in groups_ids:
					Group=group.objects.get(pk=id)
					Service.groups.add(Group)
					sg=service_group(service=Service,group=Group)
					sg.save()
					
				messages.success(request,'Successfully created a Service')
				return redirect('/accounts/signin')
			else:
				return render(request,'ServiceForm.html',{'form':form,'name':'Travel '})
		
		elif request.session['category']=='Other':
			form=OtherServiceForm(request.POST)
			if form.is_valid():
				Service=form.save(commit=False)
				Service.start_time=timezone.now()
				Service.service_type=Category.objects.get(name='Other')
				Service.initiator=request.user
				Service.save()
				groups_ids=request.session['servicegroups']
				Service.members.add(request.user)
				sm=service_member(service=Service,user=request.user)
				sm.save()
				for id in groups_ids:
					Group=group.objects.get(pk=id)
					Service.groups.add(Group)
					sg=service_group(service=Service,group=Group)
					sg.save()
					
				messages.success(request,'Successfully created a Service')
				return redirect('/accounts/signin')
			else:
				return render(request,'ServiceForm.html',{'form':form,'name':' '})

