from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import labourregisterform,Managerregisterform
from django.contrib.auth import logout,login
from django.views.generic import CreateView
from LMS.models import User
"""def labour_register(request):
    if request.method== 'POST':

       form=labourregisterform(request.POST)
       if form.is_valid():
           form.save()
           username=form.cleaned_data.get('username')
           messages.success(request,f'Account created for {username}!')
           return redirect('LMS-labour_login')
    else:
        form =labourregisterform()
    return render(request,'labour/register.html',{'form':form})
"""


class labourregisterview(CreateView):
    model=User
    form_class=labourregisterform
    template_name='labour/register.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'labour'
        return super().get_context_data(**kwargs)
  
    def form_valid(self, form):
        user = form.save()
        return redirect('LMS-labour_login')

class managerregisterview(CreateView):
    model = User
    form_class = Managerregisterform
    template_name='labour/register.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'manager'
        return super().get_context_data(**kwargs)
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('LMS-manager_login')
    



@login_required
def labour_profile(request):
    return render(request,'labour/profile.html',{'user':request.user})

@login_required
def labour_logout(request):
    logout(request)
    return redirect('LMS-home')







