from asgiref.sync import async_to_sync, sync_to_async

from channels.layers import get_channel_layer

from django import forms
from django.contrib import admin
from django.contrib.auth.models import User
from django.http import HttpRequest
from django.http.response import HttpResponse, HttpResponseRedirect
from django.urls.resolvers import URLPattern
from django.urls import path

from .models import Notification
from .tasks import send_notification_task

admin.site.register(Notification)