from django.contrib import admin
from django.urls import path, include
from notification.consumer import NotificationConsumer

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('notification/', include('notification.urls'))
]

websocket_urlpatterns = [
    path("ws/", NotificationConsumer.as_asgi())
]