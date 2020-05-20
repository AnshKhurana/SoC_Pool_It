
from django import forms
from main.models import Message
from accounts.models import User



class ChatForm(forms.ModelForm):

	class Meta:
		model = Message
		fields = ['content']
		widgets = {
			'text': forms.TextInput(attrs={
				'id': 'post-message',
				'required': True,
				'placeholder': 'Type your message...',
			}),
		}