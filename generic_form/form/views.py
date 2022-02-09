
from .models import Student
from .forms import StudentForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView


# Create your views here.
class StudentListView(ListView):
    model = Student

class StudentDetailView(DetailView):
    model = Student

class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'form/form.html'
    # fields = ['name','email','password']
    success_url = 'thanks'

class StudentTemplate(TemplateView):
    template_name = 'form/thanks.html'

class Studentupdate(TemplateView):
    template_name = 'form/thanksupdate.html'

class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'form/form.html'
    success_url = '/thanksupdate/'

class StudentDeleteView(DeleteView):
    model = Student
    success_url = '/student'


