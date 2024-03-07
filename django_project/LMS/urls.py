from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='LMS-home'),
    path('about/',views.about,name='LMS-about'),
    path('services/',views.services,name='LMS-services'),
    path('contact/',views.contact,name='LMS-contact'),
    path('manager_login/',views.manager_login,name='LMS-manager_login'),
    path('labour_login/',views.labour_login,name='LMS-labour_login'),
    path('labour_logout/',views.labour_logout,name='LMS-labour_logout'),
    path('labour_profile/',views.labour_profile,name='LMS-labour_profile'),
]