from django import forms
from main.models import group,Category
from accounts.models import User
from django.forms.widgets import CheckboxSelectMultiple 

class groupsform(forms.Form):

	def __init__(self,*args,**kwargs):
		user=kwargs.pop('user',None)
		super().__init__(*args,**kwargs)
		self.fields['groups_list'].queryset=group.objects.filter(members=user)

	groups_list=forms.ModelMultipleChoiceField(queryset=None,required=True,label='Select groups to post the service:',widget=CheckboxSelectMultiple)

	category=forms.ModelChoiceField(queryset=Category.objects.all(),required=True,label='Choose the Category:',initial=Category.objects.get(pk=1))




#class FoodServiceForm(forms.ModelForm):