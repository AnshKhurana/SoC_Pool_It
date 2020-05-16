from accounts.models import User
from main.models import group, group_member, Category, service_group


#create users

u1=User.objects.create_user(username='megha', email='a@bc.com', mobile='+1234567890', password='Abcd123$')
u1.save()
u2=User.objects.create_user(username='megha1', email='x@bc.com', mobile='+1234567891', password='Abcd123$')
u2.save()
u3=User.objects.create_user(username='megha2', email='y@bc.com', mobile='+1234567893', password='Abcd123$')
u3.save()

#create groups
g1=group(admin=u1, name='g1', description='d1', hash='#124567')
g1.save()
g2=group(admin=u2, name='g2', description='d2', hash ='#333378abc')
g2.save()
g3=group(admin=u3,name='g3', description='d2',hash = '#r4445ecg5')
g3.save()

# add members to groups
gm1= group_member(group_id=g1, user_id=u1)
gm1.save()
gm12 = group_member(group_id=g2, user_id=u1)
gm12.save()
gm2= group_member(group_id=g2, user_id=u2)
gm2.save()
gm3 = group_member(group_id=g1, user_id=u3)
gm3.save()
gm4= group_member(group_id=g2, user_id=u3)
gm4.save()
gm5= group_member(group_id=g3, user_id=u3)
gm5.save()

#initialize categories for services
c1= Category(name='Food')
c1.save()
c1= Category(name='Travel')
c1.save()
c1= Category(name='Shopping')
c1.save()
c1= Category(name='Event')
c1.save()
c1= Category(name='Other')
c1.save()

