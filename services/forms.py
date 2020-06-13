from django import forms
from main.models import group,Category,FoodService,EventService,ShoppingService,TravelService,OtherService
from accounts.models import User
from django.forms.widgets import CheckboxSelectMultiple,RadioSelect 
from django.contrib.admin import widgets
from django.utils import timezone
from django.utils.translation import gettext as _

class groupsform(forms.Form):

	def __init__(self,*args,**kwargs):
		user=kwargs.pop('user',None)
		super().__init__(*args,**kwargs)
		self.fields['groups_list'].queryset=group.objects.filter(members=user)


	Choices=[('Food','Food'),('Event','Event'),('Shopping','Shopping'),('Travel','Travel'),('Other','Other')]
	
	groups_list=forms.ModelMultipleChoiceField(queryset=None,label='Select groups to post the service:',widget=CheckboxSelectMultiple(attrs={'class':'group_checkbox'}))
	
	category=forms.ChoiceField(choices=Choices,label='Choose a Category:' ,widget=RadioSelect)



class FoodServiceForm(forms.ModelForm):

	class Meta:
		model=FoodService
		fields=['service_desc','vendor','end_time']
		widgets={
			'service_desc':forms.Textarea(attrs={'placeholder':'Describe about the service'}),
			'vendor':forms.Textarea(attrs={'placeholder':'Describe about the vendor/ place/ etc'}),
			'end_time':forms.DateTimeInput(attrs={'placeholder':'eg.; 2020-06-24 14:30 '})
		}

		labels={
			'service_desc':'Description',
			'vendor':'Vendor Description'
		}


	def clean_end_time(self): 
		data=self.cleaned_data['end_time']
		if data<=timezone.now():
			raise forms.ValidationError(_('Ending time can not be before starting time'),code='Invalid')
		return data


class ShoppingServiceForm(forms.ModelForm):
	
	
	class Meta:
		model=ShoppingService
		fields=['service_desc','vendor','end_time']
		widgets={
			'service_desc':forms.Textarea(attrs={'placeholder':'Describe about the service'}),
			'vendor':forms.Textarea(attrs={'placeholder':'Describe the service'}),
			'end_time':forms.DateTimeInput(attrs={'placeholder':'eg.; 2020-06-24 14:30 '})
		}

		labels={
			'service_desc':'Description',
			'vendor':'Vendor Description'
		}

	def clean_end_time(self): 
		data=self.cleaned_data['end_time']
		if data<=timezone.now():
			raise forms.ValidationError(_('Ending time can not be before starting time'),code='Invalid')
		return data
	

class EventServiceForm(forms.ModelForm):
	
	class Meta:
		model=EventService
		fields=['event_type','location','service_desc','end_time']
		widgets={
			'event_type': forms.RadioSelect(attrs={'class':'events_type'}),
			'service_desc':forms.Textarea(attrs={'placeholder':'Describe about the service'}),
			'location':forms.Textarea(attrs={'placeholder':'Add the location of Event'}),
			'end_time':forms.DateTimeInput(attrs={'placeholder':'eg.; 2020-06-24 14:30 '})
		}

		labels={
			'service_desc':'Description'
			
		}


	def clean_end_time(self): 
		data=self.cleaned_data['end_time']
		if data<=timezone.now():
			raise forms.ValidationError(_('Ending time can not be before starting time'),code='Invalid')
		return data

class TravelServiceForm(forms.ModelForm):
	
	class Meta:
		model=TravelService
		fields=['transport','start_point','end_point','service_desc','end_time']
		widgets={
			'transport': forms.RadioSelect(),
			'service_desc':forms.Textarea(attrs={'placeholder':'Describe about the service'}),
			'start_point':forms.Textarea(attrs={'placeholder':'Starting point address'}),
			'end_point':forms.Textarea(attrs={'placeholder':'Ending point address'}),
			'end_time':forms.DateTimeInput(attrs={'placeholder':'eg.; 2020-06-24 14:30 '})
		}
		
		labels={
			'service_desc':'Description',
			'start_point':'Pick up location',
			'end_point':'Drop location'
		}

		initial = {
			'transport': 'Taxi',
			}

	def clean_end_time(self): 
		data=self.cleaned_data['end_time']
		if data<=timezone.now():
			raise forms.ValidationError(_('Ending time can not be before starting time'),code='Invalid')
		return data

class OtherServiceForm(forms.ModelForm):
	
	class Meta:
		model=OtherService
		fields=['service_desc','end_time']
		widgets={
			'service_desc':forms.Textarea(attrs={'placeholder':'Describe about the service'}),
			'end_time':forms.DateTimeInput(attrs={'placeholder':'eg.; 2020-06-24 14:30 '})
		}

		labels={
			'service_desc':'Description'
		}
	
	def clean_end_time(self): 
		data=self.cleaned_data['end_time']
		if data<=timezone.now():
			raise forms.ValidationError(_('Ending time can not be before starting time'),code='Invalid')
		return data


		