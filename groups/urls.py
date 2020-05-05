from django.urls import path
from . import views 

urlpatterns = [
    path('group_creation', views.group_creation, name='group_creation'),
]