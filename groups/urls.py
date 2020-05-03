from django.urls import path
from . import views 

urlpatterns = [
    path('goup_creation', views.group_creation, name='group_creation'),
]