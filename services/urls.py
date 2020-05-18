from django.urls import path
from . import views

app_name='services'

urlpatterns=[
	path('servicegroups/',views.servicegroups,name='servicegroups'),
	path('createservice/',views.createservice,name='createservice'),
	path('services_available/',views.services_available, name="services_available"),
]