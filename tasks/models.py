from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Tasks(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=128)
    category = models.CharField(max_length=128)
    completed = models.CharField(max_length=3)
