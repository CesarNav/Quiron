"""Quiron URL Configuration """
from django.contrib import admin
from django.urls import path

""" Quiron apps views """
from users import views as users_views

urlpatterns = [
    path('admin/', admin.site.urls),
    
]
