from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from notification.consumer import NotificationConsumer

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('notification/', include('notification.urls'))
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

websocket_urlpatterns = [
    path("ws/", NotificationConsumer.as_asgi())
]