from django import forms
from django.forms import fields, widgets
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name','email','password']
        widgets = {'password' : forms.PasswordInput(render_value=True)}