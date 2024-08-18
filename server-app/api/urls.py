from django.urls import path, include

from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register('devices', views.DeviceView, )
router.register('logs', views.LogView, )

urlpatterns = [
    path('v1/', include(router.urls)),
]
