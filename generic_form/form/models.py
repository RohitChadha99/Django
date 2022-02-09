from django.db import models
from django.db.models.base import Model

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    password = models.CharField(max_length=10)