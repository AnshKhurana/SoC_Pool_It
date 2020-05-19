from django.urls import path,re_path
from . import views

app_name='services'

urlpatterns=[
	path('servicefilter/',views.servicefilterview.as_view(),name='servicefilter'),
	path('servicegroups/',views.servicegroups,name='servicegroups'),
	path('createservice/',views.createservice,name='createservice'),
]