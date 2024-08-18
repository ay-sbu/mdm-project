from django.shortcuts import render
from django.contrib.auth.models import User
from django.core.cache import cache

from rest_framework import viewsets, permissions

from .models import Device, Log
from .serializers import DeviceSerializer, LogSerializer

class DeviceView(viewsets.ModelViewSet):
    queryset = cache.get('django_model_all_devices')
    if not queryset:
        queryset = Device.objects.all()
        cache.set('django_model_all_devices')
    
    serializer_class = DeviceSerializer
    permission_classes = [permissions.IsAdminUser]

class LogView(viewsets.ModelViewSet):
    queryset = Log.objects.all()
    serializer_class = LogSerializer
    permission_classes = [permissions.IsAdminUser]