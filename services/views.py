from django.shortcuts import render,redirect
from main.models import group
from services.forms import groupsform

	
def groupservice(request):
	form=groupsform(user=request.user)
	return render(request,'servicegroups.html',{'form':form})

def serviceinfo(request):
	if request.method=='POST':
		request.session['servicegroups']=request.POST['groups_list']
		if request.POST['category']=='FoodService':


		if request.POST['category']=='EventService':


		if request.POST['category']=='ShoppingService':

		
		if request.POST['category']=='TravelService':
