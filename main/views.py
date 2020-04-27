from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def feed(request):

    password = request.POST['pass']
    username = request.POST['username']

    return render()