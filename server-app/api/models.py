import uuid
from django.db import models
from django.contrib.auth.models import User

class Device(models.Model):
    device_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    device_name = models.CharField(max_length=50)
    device_type = models.CharField(max_length=50)
    os_version = models.CharField(max_length=50)
    device_user = models.ForeignKey(User, on_delete=models.CASCADE)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return "{Device: name: " + self.device_name + ", user: " + self.device_user.username + "}"

class Log(models.Model):
    log_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    log_level = models.CharField(max_length=50)
    message = models.TextField()
    # created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return "{Log: kind: " + self.log_level + ", content: " + self.message + "}"