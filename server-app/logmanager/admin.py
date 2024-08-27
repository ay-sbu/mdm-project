from django.contrib import admin
from django.http.response import HttpResponse

# Register your models here.

@admin.site.register_view('logs')
def logs_view(request):
    if request.method == 'GET':
        return HttpResponse('some message')
    