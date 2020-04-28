from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import auth
from .models import User


# Create your views here.

def signin(request):
    username = request.POST['username']
    password = request.POST['pass']

    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return render(request, 'home.html')
    else:
        messages.info(request, 'invalid credentials')
        return redirect('/')


def signup(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        mobile = request.POST['mobile_number']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username taken')
                return redirect('signup')
            elif User.objects.filter(mobile=mobile).exists():
                messages.info(request, 'phone number taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, password=password1, first_name=first_name, last_name=last_name, mobile=mobile)
                user.save()
                print('user created')
                return redirect('/')
        else:
            messages.info(request, 'password not matching..')
            return redirect('signup')

        return redirect('/')

    else:    
        return render(request,'signup.html')

def signout(request):
    auth.logout(request)
    return redirect('/')

def forgot(request):
    return render(request, 'forgot.html')