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
        'user',
        )
        widget= {'date_birth': forms.DateInput}

        
        labels = {'name':'Nombre',
        'last_name':'Apellido',
        'id_type':'Tipo de documento',
        'id_number':'Numero de documento',
        'date_birth':'Fecha de nacimiento',
        'age':'Edad',
        'gender':'Genero', 
        'civil_state': 'Estado civil', 
        'ocupation' : 'Ocupacion',
        'schoolarchip' : 'Escolaridad',
        'telephone': 'Telefono', 
        'adress':'Direccion', 
        'email': 'Correo electronico',
        'user' : 'Terapeuta'
        }


        

