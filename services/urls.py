from django.urls import path,re_path
from . import views

app_name='services'

urlpatterns=[
	path('servicefilter/',views.servicefilterview.as_view(),name='servicefilter'),
	path('searchfilter/',views.searchview.as_view(),name='searchfilter'),
	path('servicegroups/',views.servicegroups,name='servicegroups'),
	path('createservice/',views.createservice,name='createservice'),
]