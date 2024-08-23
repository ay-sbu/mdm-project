from django.contrib import admin
from .models import Device, Log, Command, Applicatoin

admin.site.register(Device)
admin.site.register(Log)
admin.site.register(Command)
admin.site.register(Applicatoin)