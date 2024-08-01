from django.urls import path, include

from rest_framework import routers
from rest_framework_simplejwt import views as jwt_views

from . import views

router = routers.DefaultRouter()
router.register('devices', views.DeviceView, )
router.register('logs', views.LogView, )

urlpatterns = [
    path('v1/', include(router.urls)),
    path('token/', jwt_views.TokenObtainPairView.as_view()),
    path('token/refresh', jwt_views.TokenRefreshView.as_view()),
]
