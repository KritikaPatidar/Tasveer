from django.contrib import admin
from .models import Event, Photo, CustomUser, Photographer

# Register your models here.

admin.site.register(Event)
admin.site.register(Photo)
admin.site.register(CustomUser)
admin.site.register(Photographer)