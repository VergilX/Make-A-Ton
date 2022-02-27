from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Plant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="alarms")
    name = models.CharField(max_length=32)

    def __str__(self):
        return f"Plant '{self.name}'"