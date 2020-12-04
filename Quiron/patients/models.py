from django.db import models
from django.contrib.auth.models import User

class Patient(models.Model):
    """ Patients models """

    """ Therapist Profile """
    # Link the patient to therapist profile
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # Patients Profile

    GENDER_CHOICES=[('M', 'Masculino'),
     ('F', 'Femenino'), ('O', 'Otro')]
    ID_CHOICES=[('CC', 'Cedula Ciudadania'),
     ('CE', 'Cedula Extranjeria'), ('PE', 'Pasaporte')]
    CIVIL_STATE_CHOICES=[('Soltero/a','Soltero/a'),
     ('Casado/a','Casado/a'), ('Union libre','Union libre'), ('Divorciado/a','Divorciado/a'),('Viudo/a','Viudo/a'),]
    SCHOOLARCHIP_CHOICES=[('Sin escolaridad','Sin escolaridad'),
     ('Primaria','Primaria'), ('Secundaria','Secundaria'), ('Pregrado','Pregrado'),('Postgrado','Postgrado'),]
    name = models.CharField(max_length=60, blank=False, default=None)
    id_type = models.CharField(max_length=2, choices=ID_CHOICES, default=None)
    id_number = models.IntegerField(primary_key=True, unique=True, blank=False)
    date_birth = models.DateField(editable=True, default=None)
    age = models.IntegerField(blank=True, null= False, default=None)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default=None)
    civil_state = models.CharField(max_length=12, choices=CIVIL_STATE_CHOICES, default=None)
    ocupation = models.CharField(max_length=20, blank=True, null=True)
    schoolarchip = models.CharField(max_length=20, choices=SCHOOLARCHIP_CHOICES, default=None)
    telephone = models.CharField(max_length=10)
    adress = models.CharField(max_length=50,blank=True, null=True)
    email = models.EmailField(max_length=254, default=None)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    """ Return the patient name """
    def __str__(self):
        return self.name

