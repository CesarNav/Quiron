""" Djanog modules """
from django import forms
from reports.models import Report

class Report_Form(forms.ModelForm):
    class Meta:
        model = Report
        fields = '__all__'