from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework import viewsets

from .models import Device, Log
from .serializers import DeviceSerializer, LogSerializer

class DeviceView(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer

class LogView(viewsets.ModelViewSet):
    queryset = Log.objects.all()
    serializer_class = LogSerializer
    