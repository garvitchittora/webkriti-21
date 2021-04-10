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
                if request.POST['blog-id']:
                    blog_id = request.POST['blog-id']
                    if Blog.objects.filter(id = blog_id).exists():
                        blog = Blog.objects.filter(id = blog_id).first()
                        if request.user == blog.user:
                            blog.delete()

            elif request.POST["form-value"] == "2":
                if request.FILES.get('image'): 
                    gallery = Gallery(society = society)
                    gallery.image=request.FILES.get('image')
                    if request.POST["alt"] != '':
                        gallery.alt = request.POST.get('alt')  
                    gallery.save()

            elif request.POST["form-value"] == "3":
                if request.POST['blog-id']:
                    blog_id = request.POST['blog-id']
                    if Blog.objects.filter(id = blog_id).exists():
                        blog = Blog.objects.filter(id = blog_id).first()
                        if request.user == blog.user:
                            blog.delete()

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

class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2', 'first_name','last_name')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            current_site = get_current_site(request)
            subject = 'Activate Your My Audio Blogs Account'
            message = render_to_string('registration/account_activation_email.html', {
                'user': user,
            })

            email = EmailMessage(
                        subject, message, to=[user.email]
            )
            email.content_subtype = "html"
            email.send()

            return redirect('account_activation_sent')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})