from django.shortcuts import render,redirect,get_object_or_404
from main.models import Message
from accounts.models import User
from chat.forms import ChatForm
from django.utils import timezone
from main.models import service
from django.http import HttpResponse
from django.utils import timezone

# Create your views here.
def create_message_view(request,s_id ):
    form_class = ChatForm
    form = form_class(request.POST or None)
    qs = Message.objects.all()
    service_obj = get_object_or_404(service , service_id = s_id)
    
    if request.method=='POST':
        
        message = form.save(commit=False)
        message.user = request.user
        message.service = service_obj
        message.timestamp = timezone.localtime(timezone.now())
        message.save()
        print(qs)
        form = ChatForm()
        str ='/chat/'+ s_id +'/create'
        return redirect(str)
        
            
    else:
        if request.user in service_obj.members.all():
            qs = Message.objects.filter(service = service_obj)
            return render (request,'message_create.html',{"form" : form,"obj_list": qs})
        else:
            return HttpResponse ('You have to be a member of the service to join the chat')





            
