import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser
import random
def random_string():
    return str(random.randint(0,255))

# Create your models here.

class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    mobile = models.IntegerField(null=True)
    
