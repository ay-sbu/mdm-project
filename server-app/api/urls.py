from django.urls import path, include

from rest_framework import routers

from .views import DeviceViewSet

router = routers.DefaultRouter()
router.register(r'devices', DeviceViewSet, basename='device')

urlpatterns = [
    path('v1/', include(router.urls)),
    # path('v1/logs/', views.LogView.as_view(), name='log_view')
]
