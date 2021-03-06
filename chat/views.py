from django.shortcuts import render,redirect,get_object_or_404
from main.models import service,Message
from accounts.models import User
from chat.forms import ChatForm
from django.utils import timezone
from django.http import HttpResponse
from django.utils import timezone
import json

# Create your views here.
# def create_message_view(request,s_id ):
#     form_class = ChatForm
#     form = form_class(request.POST or None)
#     service_obj = get_object_or_404(service , service_id = s_id)
    
#     if request.method=='POST':        
#         message = form.save(commit=False)
#         message.user = request.user
#         message.service = service_obj
#         message.timestamp = timezone.localtime(timezone.now())
#         message.save()
#         a = request.POST.get('content')
#         print(a)
#         form = ChatForm()
#         str ='/chat/'+ s_id +'/create'
#         return redirect(str)
        
            
#     else:
#         if request.user in service_obj.members.all():
#             qs = Message.objects.filter(service = service_obj)
#             return render (request,'message_create.html',{"form" : form,"obj_list": qs})
#         else:
#             return HttpResponse ('You have to be a member of the service to join the chat')

def chat_view(request , s_id):

    service_obj = get_object_or_404(service , service_id = s_id)
    form = ChatForm()
    if request.user in service_obj.members.all():
        qs = Message.objects.filter(service = service_obj)
        for q in qs:
            if request.user not in q.seen.all():
                q.seen.add(request.user)
            
        return render (request,'message_create.html',{"form" : form,"obj_list": qs})
    else:
        return HttpResponse ('You have to be a member of the service to join the chat')
        


def create_message(request,s_id):
    if request.method == 'POST':
        service_obj = get_object_or_404(service , service_id = s_id)
        message_text = request.POST.get('msg')
        response_data = {}
        
        message = Message(content=message_text, user=request.user , service = service_obj  )
        
        message.save()
        
        print(message)
    
        response_data['result'] = 'Create post successful!'
        response_data['pk'] = message.pk
        response_data['content'] = message.content
        response_data['timestamp'] = timezone.localtime(timezone.now()).strftime('%B %d, %Y %I:%M %p')
        response_data['user'] = message.user.username
        

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )
def service_list(request):
    u = request.user
    qs = u.ServiceMember.all()
    notifi = 'chat/notify'
    return render (request,'gotochat.html',{"obj_list": qs})



def notifications(request):
    messages = Message.objects.all()
    unseen = []
    for message in messages:
        if message.user not in message.seen.all():
            message.seen.add(message.user)
        if request.user not in message.seen.all():
            unseen.append(message)

    return render (request,'notifications.html',{"obj_list": unseen})

def clearall(request):
    messages = Message.objects.all()
    for message in messages:
        users_seen = message.seen.add(request.user)
    return redirect('/chat/notify')      

def clearone(request,m_id):
    required_message = Message.objects.filter(id = m_id).first()
    users_seen = required_message.seen.add(request.user)
    print("Trying to delete")
    return redirect('/chat/notify')     
