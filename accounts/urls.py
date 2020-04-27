from django.urls import path

from . import views

urlpatterns = [
	path('signup', views.signup, name='signup'),
    path('forgot', views.forgot, name='forgot'),
    path('signout', views.signout, name='signout'),
]