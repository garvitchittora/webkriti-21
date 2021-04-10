from django.urls import path
from .views import *
from django.views.decorators.csrf import csrf_exempt, csrf_protect 

urlpatterns = [
    path('', home, name='home'),
]