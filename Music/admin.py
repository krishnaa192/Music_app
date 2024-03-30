from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Music)
admin.site.register(Folder)
admin.site.register(Add_to_playlist)
