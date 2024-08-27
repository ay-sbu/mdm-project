from django.contrib import admin
from .models import Device, Command, Applicatoin

admin.site.register(Device)
admin.site.register(Command)
admin.site.register(Applicatoin)