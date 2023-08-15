from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path("", view=views.index,name='index'),
    path("login_func/", view=views.login_func,name='login_func'),
    path("home/", view=views.home,name='home_func'),
    
]
