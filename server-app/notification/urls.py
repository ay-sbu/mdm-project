from django.urls import path

from .views import notification_page_view
from .consumer import NotificationConsumer

urlpatterns = [
    path("", notification_page_view, name='notification_page'),
]
