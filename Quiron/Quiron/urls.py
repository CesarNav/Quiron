"""Quiron URL Configuration """
from django.contrib import admin
from django.urls import path

""" Quiron apps views """
import users.views

""" Url patterns """
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', users.views.user_home, name ='home'),
]
