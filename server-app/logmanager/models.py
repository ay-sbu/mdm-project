from django.db import models

from .db_connector import db

# Create your models here.

model_name = 'mdm_logs'

log_model = db[model_name]