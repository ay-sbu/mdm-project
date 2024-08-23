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
        return self.device_user.username + "'s " + self.device_name 

class Log(models.Model):
    log_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    log_level = models.CharField(max_length=50)
    message = models.TextField()
    # created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self) -> str:
        return self.log_level + ": " + self.message
    
class Applicatoin(models.Model):
    app_id = models.AutoField(primary_key=True)
    app_name = models.CharField(max_length=50)
    version = models.CharField(max_length=50)
    status = models.CharField(max_length=50)
    device_id = models.ForeignKey(Device, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.app_name + " in " + Device.objects.get(device_id=self.device_id)

class Command(models.Model):
    command_id = models.AutoField(primary_key=True)
    command_type = models.CharField(max_length=50)
    command_message = models.TextField()
    status = models.CharField(max_length=50)
    device_id = models.ForeignKey(Device, on_delete=models.DO_NOTHING)
    
    def __str__(self) -> str:
        return self.command_type + ': ' + self.command_message + " for " + Device.objects.get(device_id=self.device_id)