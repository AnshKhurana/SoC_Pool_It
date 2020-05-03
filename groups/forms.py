from main.models import group
from django import forms

class group_form (forms.ModelForm):
    
    class Meta:
        model  group
        fields = ['name', 'description']
