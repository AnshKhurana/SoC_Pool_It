from django.db import models
from accounts.models import User
from main.models import service
# Create your models here.
class Message1(models.Model):
    service_id = models.ForeignKey(service, on_delete=models.CASCADE)
    user =  models.ForeignKey(User,related_name='user_messages', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()

    def __str__(self):
        return self.content + " " + str(self.timestamp)