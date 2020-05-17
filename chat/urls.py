from django.urls import path
from . import views 

urlpatterns = [
    path('<s_id>/create', views.create_message_view, name='create'),
   
    
]