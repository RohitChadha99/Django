from django.urls import path
from . import views

urlpatterns = [
    path('',views.StudentCreateView.as_view(),name='form'),
    path('student/',views.StudentListView.as_view(),name='student'),
    path('student/<int:pk>',views.StudentDetailView.as_view(),name='detail'),
    path('thanks/',views.StudentTemplate.as_view(),name='thanks'),
    path('update/<int:pk>',views.StudentUpdateView.as_view(),name='update'),
    path('thanksupdate/',views.Studentupdate.as_view(),name='thanksupdate'),
    path('delete/<int:pk>',views.StudentDeleteView.as_view(),name='delete'),
]
