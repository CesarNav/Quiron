from django.db import models
from patients.models import Patient
from django.contrib.auth.models import User

""" Report Model """
class Report(models.Model):

    patient = models.ForeignKey(Patient, related_name='id_patient', on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)
    used_techniques =models.CharField(max_length=200)
    conclusions =models.CharField(max_length=200)

    def ____(self):
        return self.created