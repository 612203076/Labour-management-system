from django.shortcuts import render,redirect
from .models import Labour
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    return render(request,'LMS/home.html')

def about(request):
    return render(request,'LMS/about.html')

def services(request):
    return render(request,'LMS/services.html')

def contact(request):
    return render(request,'LMS/contact.html')

def manager_login(request):
    return render(request,'LMS/manager_login.html')


def labour_login(request):
    return render(request,'labour/labour_login.html')

@login_required
def labour_profile(request):
    return render(request, 'labour/labour_profile.html', {'user': request.user})

@login_required
def labour_logout(request):
    logout(request)
    return redirect('LMS-home')




