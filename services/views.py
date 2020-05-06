from django.shortcuts import render,redirect
from accounts.models import User
from main.models import group

	
def groupservice(request):
	user=request.user
	group_list=group.objects.filter(members=user)
	return render(request,'servicegroups.html',{'group_list':group_list})

