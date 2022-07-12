from django.db import models
# Create your models here.

class FieldsModel(models.Model):
    inputs = models.JSONField()