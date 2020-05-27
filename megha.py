from main.models import service
from accounts.models import User
from chat.models import Message1

m = Message1.objects.all()
s = service.objects.all()
u = User.objects.all()