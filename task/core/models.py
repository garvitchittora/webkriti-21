from django.db import models

from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils import timezone

from django.db.models.signals import pre_save
from django.core.validators import RegexValidator
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _

class UserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

class Society(models.Model):
    image = models.ImageField(upload_to ='society/', null=True, blank=True) 
    name = models.CharField(max_length=150, null=True, blank=True)
    bio = models.CharField(max_length=1500, null=True, blank=True)
    slug = models.SlugField(max_length=250,null=True,blank=True,unique=True)
    fb = models.URLField(max_length = 10000, null=True, blank=True)

class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    image = models.ImageField(upload_to ='user/', null=True, blank=True) 
    slug = models.SlugField(max_length=250,null=True,blank=True,unique=True)
    bio = models.CharField(max_length=1500, null=True, blank=True)
    power_value = models.IntegerField(default=0)
    society = models.ForeignKey(Society,null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        self.username = self.email
        super(User, self).save(*args, **kwargs)

class Gallery(models.Model):
    image = models.ImageField(upload_to ='gallery/', null=True, blank=True)
    alt = models.CharField(max_length=150, null=True, blank=True)
    society = models.ForeignKey(Society,null=True, blank=True, on_delete=models.SET_NULL)

class Event(models.Model):
    image = models.ImageField(upload_to ='event/', null=True, blank=True)
    bio = models.CharField(max_length=1500, null=True, blank=True)
    society = models.ForeignKey(Society,null=True, blank=True, on_delete=models.SET_NULL)
    slug = models.SlugField(max_length=250,null=True,blank=True,unique=True)
    name = models.CharField(max_length=150, null=True, blank=True)

def createSlug(instance,text,new_slug=None):
    slug=slugify(text)
    if new_slug is not None:
        slug=new_slug

    qs=Society.objects.filter(slug=slug).order_by("-id")
    exists=qs.exists()
    if exists and qs.first() != instance:
        new_slug="%s-%s" %(slug , qs.count())
        return createSlug(instance,text,new_slug=new_slug)             
    return slug

def generateSlugSociety(sender,instance,*arg,**k):
    instance.slug=createSlug(instance,instance.name)

pre_save.connect(generateSlugSociety,sender=Society)

def generateSlugEvent(sender,instance,*arg,**k):
    instance.slug=createSlug(instance,instance.name)

pre_save.connect(generateSlugEvent,sender=Event)

def generateSlugUser(sender,instance,*arg,**k):
    instance.slug=createSlug(instance,instance.get_full_name())

pre_save.connect(generateSlugUser,sender=User)