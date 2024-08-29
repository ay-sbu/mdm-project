from asgiref.sync import async_to_sync, sync_to_async

from channels.layers import get_channel_layer

from django import forms
from django.contrib import admin
from django.contrib.auth.models import User
from django.http import HttpRequest
from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls.resolvers import URLPattern
from django.urls import path

from .mqtt import client as mqtt_client

class SendMQTTNotificationForm(forms.Form):
    message = forms.CharField(label="message", max_length=200)
    # topic_name = forms.CharField(label="topic_name", max_length=200)


@admin.site.register_view('send_mqtt_notif')
def send_mqtt_notif_view(request):
    context = {}
    
    if request.method == 'POST':
        form = SendMQTTNotificationForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data["message"]
            # topic_name = form.cleaned_data["topic_name"]
                            
            rc, mid = mqtt_client.publish('ay/commands', message)
            
            form = SendMQTTNotificationForm()
            
            context["form"] = form
            context['success'] = True
            
            return render(request, 'admin/notif_form.html', context)
    else:
        form = SendMQTTNotificationForm()
    
    context["form"] = form
        
    return render(request, 'admin/custom_add_form.html', context)
    