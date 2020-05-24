from django.urls import path
from . import views 
app_name='chat'
urlpatterns = [
    path('<s_id>/chatroom/', views.chat_view, name='chatroom'),
    path('<s_id>/chatroom/create', views.create_message, name='create'),
    path('servicelist', views.service_list, name='listout'),
   
    
]