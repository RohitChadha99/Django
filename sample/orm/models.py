from django.db import models
from django.db.models.deletion import CASCADE


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Info(models.Model):
    student = models.OneToOneField(Student,on_delete=CASCADE)
    roll = models.IntegerField()

class Skill(models.Model):
    skill_name = models.CharField(max_length=20)
    student = models.ManyToManyField(Student)

class Contact(models.Model):
    phone_no = models.IntegerField()
    student = models.ForeignKey(Student,on_delete=CASCADE,blank=True)

