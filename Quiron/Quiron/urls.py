"""Quiron URL Configuration """
from django.contrib import admin
from django.urls import path

""" Quiron apps views """
from users import views as users_views
from patients import views as patients_views


""" Url patterns """
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', users_views.home, name ='home'),
    path('login/', users_views.login_view, name ='login'),
    path('logout/', users_views.logout_view, name ='logout'),
    path('signin/', users_views.signin_view, name ='signin'),
    path('profile', users_views.user_profile, name ='profile'),
    path('profile/update/', users_views.prof_update, name ='prof_update'),
    path('patient_creation/', patients_views.patient_creation, name ='patient_creation'),
    path('patient/<int:id_number>/', patients_views.patient_profile, name ='patient_profile'),
    path('patient_update/<int:id_number>/', patients_views.patient_update, name ='patient_update'),
    path('patient_deactivate/<int:id_number>/', patients_views.patient_deactivate, name ='patient_deactivate'),
    path('patient_delete/<int:id_number>/', patients_views.patient_delete, name ='patient_delete'),
]




