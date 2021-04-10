from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    societies = Society.objects.all()
    
    for society in societies:
        society.coordi = User.objects.filter(society=society).all()

    data = {
        "society":societies
    }

    return render(request, "home.html",data)

def societyPage(request,slug):
    societies = Society.objects.all()
    
    data = {
        "society":societies
    }

    return render(request, "society.html",data)

def userPage(request,slug):
    societies = Society.objects.all()
    
    data = {
        "society":societies
    }
    if User.objects.filter(slug=slug).exists():

        return render(request, "society.html",data)

    return render(request, "404.html",data)   