from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('<int:student_id>/info',views.info,name='info'),
    path('<int:student_id>/contact',views.contact,name='contact'),
    path('<int:student_id>/skill',views.skill,name='skill'),
    ]