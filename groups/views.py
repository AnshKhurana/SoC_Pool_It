from django.shortcuts import render, redirect
from .forms import group_form
from main.models import group, group_member

# Create your views here.

def group_creation(request):
    if request.method=='POST':
        form = group_form(request.POST)
        if form.is_valid():
           

    else:
        form = group_form()
        return render(request, 'group_creation.html', {'form':form})

