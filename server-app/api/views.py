from django.shortcuts import render
from django.contrib.auth.models import User
from django.core.cache import cache

from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Log
from .serializers import LogSerializer

class LogView(APIView):
    def post(self, request, format=None):
        serializer = LogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)