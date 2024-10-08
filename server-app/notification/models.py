from django.db import models
from django.contrib.auth.models import User

class Notification(models.Model):
    message = models.TextField()
    target_user = models.ForeignKey(User, null=True, on_delete=models.DO_NOTHING)
    status = models.CharField(max_length=50, default='SEEN')
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, null=True)

    def __str__(self) -> str:
        return "{ Notification: message: " + self.message + " }"
