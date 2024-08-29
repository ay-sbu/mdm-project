from django.shortcuts import render
from django.contrib.auth.models import User
from django.core.cache import cache

from rest_framework import permissions, status, viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from .models import Device
from .serializers import DeviceSerializer

class DeviceViewSet(viewsets.ModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceSerializer
    permission_classes = [IsAdminUser, IsAuthenticated]

    def get_queryset(self):
        return self.queryset.filter(device_user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(device_user=self.request.user)