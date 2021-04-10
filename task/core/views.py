from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect

from .models import *

# Create your views here.

def home(request):
    societies = Society.objects.all()
    
    for society in societies:
        society.coordi = User.objects.filter(society=society,power_value = 1).all()

    data = {
        "society":societies
    }

    return render(request, "home.html",data)

def societyPage(request,slug):
    societies = Society.objects.all()
    
    if Society.objects.filter(slug=slug).exists():
        society = Society.objects.filter(slug=slug).first()
        
        if request.method == "POST" and ( request.user.power_value == 1 or request.user.power_value == 0 ):
            if request.POST["form-value"] == "0":
                if request.POST['name'] != '':
                    society.name = request.POST['name']
                if request.POST['fb'] != '':
                    society.fb = request.POST['fb']
                if request.FILES.get('image'):   
                    society.image=request.FILES.get('image')
                if request.POST.get('bio', False) and request.POST["bio"] != 'None':
                    society.bio = request.POST.get('bio')  
                society.save()  
            elif request.POST["form-value"] == "1":
                user = User(society = society)
                if request.POST['firstName'] != '':
                    user.first_name = request.POST['firstName']   
                if request.POST['lastName'] != '':
                    user.last_name = request.POST['lastName']
                if request.POST['email'] != '':
                    user.email = request.POST['email']  
                if request.POST['password'] != '':
                    user.set_password(request.POST['password'])
                if request.POST['type'] != '':
                    user.power_value = request.POST['type']  
                if request.FILES.get('image'):   
                    user.image=request.FILES.get('image')
                if request.POST.get('bio', False) and request.POST["bio"] != 'None':
                    user.bio = request.POST.get('bio')  
                user.save()

            elif request.POST["form-value"] == "2":
                if request.FILES.get('image'): 
                    gallery = Gallery(society = society)
                    gallery.image=request.FILES.get('image')
                    if request.POST["alt"] != '':
                        gallery.alt = request.POST.get('alt')  
                    gallery.save()

            elif request.POST["form-value"] == "3":
                event = Event(society = society)
                if request.POST['name'] != '':
                    event.name = request.POST['name']
                if request.FILES.get('image'):   
                    event.image=request.FILES.get('image')
                if request.POST.get('bio', False) and request.POST["bio"] != 'None':
                    event.bio = request.POST.get('bio')  
                event.save()

        data = {
            "society":societies,
            "societyData": society,
            "coordi": User.objects.filter(society=society,power_value = 1).all(),
            "member": User.objects.filter(society=society,power_value = 2).all(),
            "membersCount":User.objects.filter(society=society).all().count,
            "gallery": Gallery.objects.filter(society=society).all(),
            "event": Event.objects.filter(society=society).all(),
        }
        return render(request, "society.html",data)

    data = {
        "society":societies
    }

    return render(request, "404.html",data)  

def account_activation_sent(request):
    return render(request, 'registration/account_activation_sent.html')