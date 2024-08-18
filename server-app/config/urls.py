from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from notification.consumer import NotificationConsumer

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('notification/', include('notification.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]

websocket_urlpatterns = [
    path("ws/", NotificationConsumer.as_asgi())
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)