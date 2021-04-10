from django.urls import path
from .views import *
from django.views.decorators.csrf import csrf_exempt, csrf_protect 

urlpatterns = [
    path('', home, name='home'),
    path('society/<slug>', societyPage , name = "societyPage"),
    path('signup/', signup, name='signup'),
    path('account_activation_sent/', account_activation_sent, name='account_activation_sent'),
]