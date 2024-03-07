from django.db import models
from django.contrib.auth.models import User
from LMS.models import Labour

class Profile(models.Model):
    labour=models.OneToOneField(Labour,on_delete=models.CASCADE)
    image=models.ImageField(default='default.jpg',upload_to='profile_pics')
    
    def __str__(self):
        return  f'{self.labour.username} Profile'
# Create your models here.
    





