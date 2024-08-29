import ast

from django import forms
from django.contrib import admin
from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseBadRequest, JsonResponse

from .models import log_model, db
from .utils import parse_projection, parse_find_query

# Register your models here.

class LogQueryForm(forms.Form):
    query = forms.CharField(label="FindQuery", max_length=300, required=False)
    projection = forms.CharField(label="Projection", max_length=300, required=False)

@admin.site.register_view('log')
def logs_view(request):
    context = {}
    form = LogQueryForm(request.POST)
    context['form'] = form
    if request.method == 'GET':
        logs = list(log_model.find())
        context['logs'] = logs
        return render(request, 'admin/log_view.html', context)
    elif request.method == 'POST':
        if form.is_valid():
            query = form.data['query']
            projection = form.data['projection']
            
            query = parse_find_query(query)
            projection = parse_projection(projection)
            
            print('query', query)
            print('projection', projection)
            
            logs = list(log_model.find(query, projection))
            context['logs'] = logs
            return render(request, 'admin/log_view.html', context)
    return HttpResponseBadRequest()

