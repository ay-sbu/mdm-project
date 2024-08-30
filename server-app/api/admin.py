from django.contrib import admin
from django.contrib.auth.models import User

from .models import Device, Command, Applicatoin

admin.site.register(User)
admin.site.register(Device)
admin.site.register(Command)
admin.site.register(Applicatoin)