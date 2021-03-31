from django.db import models
from django.contrib.auth.models import User
# Create your models here.

options = [
    ('Food','food'),
    ('Clothing', 'clothing'),
    ('Housing', 'housing'),
    ('Education', 'education'),
    ('Entertainment', 'entertainment'),
    ('Other', 'other'),
]

class BudgetEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=128)
    category = models.CharField(max_length=20, choices=options)
    projected = models.CharField(max_length=20)
    actual = models.CharField(max_length=20)
