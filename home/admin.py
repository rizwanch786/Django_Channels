from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Notification)
admin.site.register(Student)
