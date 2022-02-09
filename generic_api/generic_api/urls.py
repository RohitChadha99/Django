
from django.contrib import admin
from django.urls import path
from myapi import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/',views.ListCreateApi.as_view()),
    path('student/<int:pk>',views.RetrieveUpdateDestroyApi.as_view()),
]
