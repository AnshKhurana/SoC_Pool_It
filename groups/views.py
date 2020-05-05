from django.shortcuts import render, redirect
from .forms import group_form
from main.models import group_member, group
import random, hashlib
from django.contrib import messages
from accounts.models import User

# Create your views here.

#-------------------------------------------------------------#

def hash_generator():
    hash = hashlib.md5()
    hash.update(str(random.random()).encode())
    return hash.hexdigest()[:-10]

#-------------------------------------------------------------#

def group_creation(request):
    if request.method=='POST':
        form = group_form(request.POST)
        if form.is_valid():
            
            Group = form.save(commit=False)
            Group.admin = request.user
            while(1):
                hash = hash_generator()
                if not(group.objects.filter(hash=hash).exists()):
                    Group.hash = hash
                    break
            Group.save()

            GroupMember = group_member.objects.create(group_id=Group, user_id=request.user)

            messages.info(request, 'group created')
            return redirect('/accounts/signin')
        else:
            messages.info(request, 'invalid input')
            return redirect('group_creation')

    else:
        form = group_form()
        return render(request, 'group_creation.html', {'form':form})

