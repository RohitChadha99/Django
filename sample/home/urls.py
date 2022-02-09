
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('signup',views.signup,name='signup'),
    path('<int:detail_id>/update',views.update,name='update'),
    ] 