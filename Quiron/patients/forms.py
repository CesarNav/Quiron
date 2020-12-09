""" Djanog modules """
from django import forms

""" Local modules """
from patients.models import Patient

#Create a patient form from patient model
class Patient_Form(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ('name',
        'last_name',
        'id_type',
        'id_number',
        'date_birth',
        'age',
        'gender', 
        'civil_state', 
        'ocupation', 
        'schoolarchip', 
        'telephone', 
        'adress', 
        'email',
        'user',)
        # widgets = {'name':forms.Textarea}

