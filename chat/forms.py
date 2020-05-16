
from django import forms
from .models import Message1
from accounts.models import User



class ChatForm(forms.ModelForm):

	class Meta:
		model=Message1
		fields=['content']