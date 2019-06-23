from django.contrib import admin

# Register your models here.
from app.models import *

class Admin_show(admin.ModelAdmin):
    list_display = ['name']
admin.site.register(User,Admin_show)
