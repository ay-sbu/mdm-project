from django.contrib import admin
from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseBadRequest, JsonResponse

from .models import log_model

# Register your models here.

@admin.site.register_view('log')
def logs_view(request):
    context = {}
    if request.method == 'GET':
        logs = list(log_model.find())
        context['logs'] = logs
        return render(request, 'admin/log_view.html', context)
    return HttpResponseBadRequest()