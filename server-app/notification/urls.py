from django.urls import path

from .views import notification_page_view, index_view, show_firebase_js
from .consumer import NotificationConsumer

urlpatterns = [
    path("index/", index_view, name='index'),
    path("firebase-messageing-sw.js", show_firebase_js, name='show_firebase'),
    path("", notification_page_view, name='notification_page'),
]
