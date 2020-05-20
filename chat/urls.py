from django.urls import path
from . import views 
app_name='chat'
urlpatterns = [
    path('<s_id>/chatroom', views.chat_view, name='chatroom'),
    path('<s_id>/create', views.create_message, name='create'),
   
    
]