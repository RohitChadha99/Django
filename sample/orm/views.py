from django.shortcuts import render

from .models import Student,Info,Skill,Contact


# Create your views here.
def index(request):
    # stu = Student.objects.all()
    stu = Student.objects.all()
    return render(request,'orm/index.html',{'stu':stu})

def info(request,student_id):
    r = Info.objects.filter(student=student_id)
    return render(request,'orm/info.html',{'r':r})

def contact(request,student_id):
    list = Contact.objects.filter(student=student_id)
    return render(request,'orm/contact.html',{'list':list})

def skill(request,student_id):
    s = Skill.objects.filter(student=student_id)
    return render(request,'orm/skill.html',{'s':s})