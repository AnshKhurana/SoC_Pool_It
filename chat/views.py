from django.shortcuts import render,redirect
from .models import Message1
from accounts.models import User
from chat.forms import ChatForm
from django.utils import timezone


# Create your views here.
def create_message_view(request):
    form_class = ChatForm
    form = form_class(request.POST or None)
    qs = Message1.objects.all()
    print('megha')
    print(request.method)
    if request.method=='POST':
        print('hii')
        if form.is_valid():
            print("please")
            message = form.save(commit=False)
            message.user = request.user
            print(message.user)
            message.timestamp = timezone.now()
            message.save()
            print(message.timestamp)
            qs = Message1.objects.all()

    return render (request,'message_create.html',{"form" : form,"obj_list": qs })





            
