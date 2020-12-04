# Django
from django.contrib import admin

# Import our models to the admin
from patients.models import Patient as patient

# Register the model patient in the admin

@admin.register(patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ['pk', 'user','name','id_type', 'id_number']
    search_fields = ('user__username', 'patient__name')