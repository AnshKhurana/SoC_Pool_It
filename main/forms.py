from django import forms
from .models import group

class group_form (forms.ModelForm):
    class Meta:
        model  group
        fields = ['name', 'description']