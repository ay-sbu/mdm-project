import os

from channels.routing import ProtocolTypeRouter, URLRouter

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

http_application = get_asgi_application()

from django_channels_jwt_auth_middleware.auth import JWTAuthMiddlewareStack

from . import urls

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": JWTAuthMiddlewareStack(
            URLRouter(urls.websocket_urlpatterns)
        )
    }
)
