from django.urls import path
from . import views 

urlpatterns = [
    path('group_creation', views.group_creation, name='group_creation'),
    path('join_group', views.join_group, name='join_group'),
]