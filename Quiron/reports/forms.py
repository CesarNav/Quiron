""" Djanog modules """
from django import forms
from reports.models import Report

class Report_Form(forms.ModelForm):
    class Meta:
        model = Report
        fields = '__all__'
        labels = {
            'patient':'Paciente',
            'used_techniques' : 'Técnicas utilizadas',
            'conclusions':'Conclusiones',
        }