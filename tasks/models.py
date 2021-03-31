from django.db import models
from django.contrib.auth.models import User
# Create your models here.

options = [
    ('home', 'Home'),
    ('school', 'School'),
    ('work', 'Work'),
    ('self improvement', 'Self improvement'),
    ('other', 'Other'),
]

class TasksEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=128)
    category = models.CharField(max_length=20, choices=options)
    completed = models.CharField(max_length=3, default='No')
