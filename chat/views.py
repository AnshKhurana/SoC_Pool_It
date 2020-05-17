from django.shortcuts import render,redirect,get_object_or_404
from .models import Message1
from accounts.models import User
from chat.forms import ChatForm
from django.utils import timezone
from main.models import service

# Create your views here.
def create_message_view(request,s_id = '0'):
    form_class = ChatForm
    form = form_class(request.POST or None)
    qs = Message1.objects.all()
    if request.method=='POST':
        if form.is_valid():
            print("please")
            message = form.save(commit=False)
            message.user = request.user
            message.service = get_object_or_404(service , service_id = s_id)
            print(message.user)
            message.timestamp = timezone.now()
            message.save()
            print(message.timestamp)
            qs = Message1.objects.all()
            form = ChatForm()
    return render (request,'message_create.html',{"form" : form,"obj_list": qs })





            
