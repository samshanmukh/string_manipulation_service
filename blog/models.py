from django.db import models
from django.utils import timezone

class Strings(models.Model):
   string = models.CharField(max_length=100)
   operations = models.JSONField()
   createdAt = models.DateTimeField(default=timezone.now)
   updatedAt = models.DateTimeField(default=timezone.now)