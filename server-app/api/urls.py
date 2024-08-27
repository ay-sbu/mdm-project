from django.urls import path, include

from rest_framework import routers

from . import views

router = routers.DefaultRouter()

urlpatterns = [
    path('v1/', include(router.urls)),
    # path('v1/logs/', views.LogView.as_view(), name='log_view')
]
