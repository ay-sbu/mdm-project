from django.shortcuts import render
from django.http.response import HttpResponse

from .models import log_model

# Create your views here.

def add_log_view(request):
    record = {
        "scope":  "server-app",
        "level": "INFO",
        "message": "notif sended successfully"
    }
    log_model.insert_one(record)
    return HttpResponse('new record added')

def get_log_view(request):
    logs = log_model.find()
    return (logs)