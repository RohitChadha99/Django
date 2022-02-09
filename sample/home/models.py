from django.db import models

# Create your models here.
class Detail(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=20)
    pic=models.ImageField()