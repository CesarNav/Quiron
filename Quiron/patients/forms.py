""" Djanog modules """
from django import forms

""" Local modules """
from patients.models import Patient

#Create a patient form from patient model
class Patient_Form(forms.ModelForm):
    class Meta:
        model = Patient
        fields = '__all__'