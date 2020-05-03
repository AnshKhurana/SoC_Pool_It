from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import auth
from .models import User
#from poolit.settings import EMAIL_HOST_SERVER
from django.core import mail
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
import math, random


# Create your views here.

#--------------------------------------------------------#

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

def signout(request):
    auth.logout(request)
    return redirect('/')

#--------------------------------------------------------#

def signup(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username taken')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email address already taken')
                return redirect('signup')
            else:
                user = User.objects.create_user(username=username, password=password1, first_name=first_name, last_name=last_name, email=email)
                user.save()
                print('user created')
                return redirect('/')
        else:
            messages.info(request, 'password not matching..')
            return redirect('signup')

        return redirect('/')

    else:    
        return render(request,'signup.html')

#--------------------------------------------------------#

def forgot(request):
    '''if request.method=='POST':
        email = request.POST['email']
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            subject = 'New password for pool-it'
            password = generateOTP()
            message = 'username:'+str(user.username)+'/n'+'password:'+password

            mail.send_mail(
                subject,
                message,
                EMAIL_HOST_SERVER,
                [str(email)],
                fail_silently=False,
            )
            if len(mail.outbox)==1
            messages.info(request, 'an OTP is sent to your email id along with your username')
            render('/')
    else:'''
        return render(request, 'forgot.html')

#--------------------------------------------------------#

def change_password(request):
    if request.method=='POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was successfully updated')
            return redirect('/')
        else:
            messages.error(request, 'Please correct the error below')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {'form':form})


def update(request):
    if request.method=='POST':
        user = request.user
        last_name = request.POST['last_name']
        first_name = request.POST['first_name']
        username = request.POST['username']
        user.last_name=last_name
        user.first_name = first_name
        user.username = username
        user.save()
        return render(request, 'home.html')
    else:
        return render(request, 'update.html')

#-------------------------------------------------------#

# function to generate OTP 
def generateOTP() : 
  
    # Declare a string variable   
    # which stores all string  
    string = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    OTP = "" 
    length = len(string) 
    for i in range(6) : 
        OTP += string[math.floor(random.random() * length)] 
  
    return OTP 

#-------------------------------------------------------#
