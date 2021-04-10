from django.contrib import admin
from .models import *

# Register your models here.
class SocietyAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
admin.site.register(Society, SocietyAdmin)

class EventAdmin(admin.ModelAdmin):
    list_display = ('name',)
admin.site.register(Event, EventAdmin)

admin.site.register(User)
admin.site.register(Gallery)
