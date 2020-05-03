from django.urls import path

from . import views

urlpatterns = [
	path('signup', views.signup, name='signup'),
    path('forgot', views.forgot, name='forgot'),
    path('signout', views.signout, name='signout'),
    path('signin', views.signin, name='signin'),
    path('change_password', views.change_password, name='change_password'),
    path('update_details', views.update, name='update_details'),
]