from django.contrib import admin

# Import our models to the admin
from reports.models import Report as report

# Register the report model in the admin

@admin.register(report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ['patient', 'created',]
    search_fields = ('patient', 'created',)
