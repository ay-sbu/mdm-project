from asgiref.sync import async_to_sync

from channels.layers import get_channel_layer

from django.contrib import admin
from django import forms
from django.http import HttpRequest
from django.http.response import HttpResponse, HttpResponseRedirect
from django.urls.resolvers import URLPattern
from django.urls import path

from .models import Notification
from .tasks import send_notification_task

class SendNotificationForm(forms.Form):
    message = forms.CharField(label="Notification Message", max_length=200)
    
@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    add_form_template = "admin/custom_add_form.html"

    def add_view(self, request: HttpRequest, form_url: str = '', extra_context: None = ...) -> HttpResponse:
        if request.method == "POST":
            form = SendNotificationForm(request.POST)
            if form.is_valid():
                message = form.cleaned_data["message"]

                notification = Notification.objects.create(message=message)
                
                # DEBUG: NOT USING CELERY
                # channel_layer = get_channel_layer()
                # async_to_sync(channel_layer.group_send)(
                #     "all",
                #     {
                #         "type": "send_notification",
                #         "message": message
                #     }
                # )
                                
                # USING CELERY
                send_notification_task.delay(message)
                
                return HttpResponseRedirect("../{}/".format(notification.pk))
        else:
            form = SendNotificationForm()
        
        context = self.get_changeform_initial_data(request)
        context["form"] = form
        return super().add_view(request, form_url, context)

    def get_urls(self) -> list[URLPattern]:
        urls = super().get_urls()
        custom_url = [
            path("send-notification/", self.admin_site.admin_view(self.add_view), name="send-notification"),
        ]
        return custom_url + urls