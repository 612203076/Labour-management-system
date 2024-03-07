from django.contrib import admin

# Register your models here.
from .models import Profile
from LMS.models import Trades
admin.site.register(Trades)

admin.site.register(Profile)
