from django.db import models
from django.contrib.auth.models import AbstractUser,Group, Permission
# Create your models here.

 


class User(AbstractUser):
    is_labour = models.BooleanField(default=False)
    is_manager = models.BooleanField(default=False)

    class Meta:
        db_table = 'user'

# Add related_name arguments to resolve clashes
User.groups.field.remote_field.related_name = 'user_groups'
User.user_permissions.field.remote_field.related_name = 'user_permissions_set'


"""class User(AbstractUser):
    username=models.CharField(max_length=15)
    email=models.CharField(max_length=20,null=False,default=None)
    password = models.CharField(max_length=128) 
    image = models.ImageField(upload_to='django_project\LMS\static\LMS\profile_pics',default='django_project\LMS\static\LMS\profile_pics\default.jpg')
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # Add additional manager-specific fields here, if needed

    def __str__(self):
        return self.user.username
"""    

class Trades(models.Model):
    trade=models.CharField(max_length=15,null=True)
    def __str__(self):
        return self.trade



class Labour(models.Model):
    """username=models.CharField(max_length=15)
    email=models.CharField(max_length=20,null=True)
    password = models.CharField(max_length=128) 
    """
    image = models.ImageField(upload_to='django_project\LMS\static\LMS\profile_pics',default='django_project\LMS\static\LMS\profile_pics\default.jpg')
    user = models.ForeignKey(User, on_delete=models.CASCADE)   #cascade means if the manger instance is deleted the labour instances associated with that manager will get deleted
    trade = models.ForeignKey(Trades, on_delete=models.CASCADE,default=None) 
    # Add additional manager-specific fields here, if needed

    def __str__(self):
        return f"Labour-{self.user.username}-{self.user.email}-{self.trade.trade}"


