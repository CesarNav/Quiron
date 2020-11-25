from django.db import models
from django.contrib.auth.models import User

class Patient(models.Model):
    """ Patients models

    Proxy model extends the base data with other information.
    """
    #user = models.OneToOneField(User, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.PROTECT)

    #Terapist Profile
    profile = models.ForeignKey('users.Profile', on_delete=models.PROTECT)

    GENDER_CHOICES=[('M', 'Male'), ('F', 'Female')]
    ID_CHOICES=[('CC', 'Cedula Ciudadania'), ('CE', 'Cedula Extranjeria'), ('TI', 'Tarjeta Identidad')]
    id_type = models.CharField(max_length=2, choices=ID_CHOICES, null=False)
    id_number = models.CharField(max_length=20, unique=True, blank=False, null=False )
    age = models.IntegerField(blank=True, null= False )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank= True)
    civil_state = models.CharField(max_length=10, blank=True, null=True)
    ocupation = models.CharField(max_length=20, blank=True, null=True)
    telephone = models.CharField(max_length=10)
    adress = models.CharField(max_length=50,blank=True, null=True)

    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    """ Return the patient name """
    def __str__(self):
        return self.user.first_name

