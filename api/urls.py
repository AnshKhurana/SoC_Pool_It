from django.urls import path
from .views import *

urlpatterns=[
	path('servicefilter/',servicefilterview.as_view(),name='servicefilter'),
	path('addservicemember/',add_service_member,name='add_service_member'),
]