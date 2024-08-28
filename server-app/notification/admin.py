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

from .models import Notification
from .tasks import send_notification_task

admin.site.register(Notification)


class SendNotificationForm(forms.Form):
    message = forms.CharField(label="message", max_length=200)
    # target_user = forms.CharField(label="target_user", max_length=200)
    target_user = forms.ModelChoiceField(label="target_user", queryset=User.objects.all())


@admin.site.register_view('send_notif')
def send_notif_view(request):
    context = {}
    
    if request.method == 'POST':
        form = SendNotificationForm(request.POST)
        if form.is_valid():
            message = form.cleaned_data["message"]
            target_user = form.cleaned_data["target_user"]
            
            selected_user = User.objects.filter(username=target_user.username)

            if selected_user.count() > 0:
                notification = Notification.objects.create(message=message, target_user=selected_user.first())
                                
                send_notification_task.delay(message, selected_user.first().username)
                
                form = SendNotificationForm()
                
                context["form"] = form
                context['success'] = True
                
                return render(request, 'admin/custom_add_form.html', context)
    else:
        form = SendNotificationForm()
    
    context["form"] = form
        
    return render(request, 'admin/custom_add_form.html', context)
    