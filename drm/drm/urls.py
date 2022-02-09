
from django.contrib import admin
from django.urls import path , include
from api import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('studentapi/',views.Student_api,name='studentapi'),
    path('studentdetail/',views.Student_detail,name='studentdetail'),
]
