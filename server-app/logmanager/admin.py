from django.contrib import admin
from django.http.response import HttpResponse, HttpResponseBadRequest, JsonResponse

from .models import log_model

# Register your models here.

@admin.site.register_view('log')
def logs_view(request):
    if request.method == 'GET':
        logs = list(log_model.find())
        return HttpResponse(logs)
    if request.method == 'POST':
        record = {
            "scope":  "server-app",
            "level": "INFO",
            "message": "notif sended successfully"
        }
        log_model.insert_one(record)
        return HttpResponse('new record added') 
    return HttpResponseBadRequest()