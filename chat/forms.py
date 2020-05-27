
from django import forms
from main.models import Message
from accounts.models import User
from django.contrib.admin import widgets


class ChatForm(forms.ModelForm):

	class Meta:
		model=Message
		fields=['content']
		widgets = {
            'content': forms.TextInput(attrs={
                'id': 'post-text', 
                'required': True, 
                'placeholder': 'Say something...'
            }),
        }