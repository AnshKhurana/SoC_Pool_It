from django.shortcuts import render,redirect
from main.models import group,Category,service_group,service_member			
from services.forms import groupsform,FoodServiceForm,EventServiceForm,TravelServiceForm,ShoppingServiceForm,OtherServiceForm
from django.utils import timezone
from django.contrib import messages



def servicegroups(request):
	
	if request.method=="POST":
		
		form=groupsform(request.POST,user=request.user)
		
		if form.is_valid():
			c=list(form.cleaned_data['groups_list'].values_list('group_id',flat=True))
			request.session['servicegroups']=[str(o) for o in c ]

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
				for id in groups_ids:
					Group=group.objects.get(pk=id)
					Service.groups.add(Group)
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

