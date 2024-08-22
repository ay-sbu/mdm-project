from django.db import models
from django.contrib.auth.models import User

class Notification(models.Model):
    message = models.TextField()
    target_user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return "{ Notification: message: " + self.message + " }"
