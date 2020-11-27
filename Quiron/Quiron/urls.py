"""Quiron URL Configuration """
from django.contrib import admin
from django.urls import path

""" Quiron apps views """
from users import views as users_views

""" Url patterns """
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', users_views.home, name ='home'),
    path('login/', users_views.login_view, name ='login'),
]
