""" Modules """
# Djanog modules
from django.shortcuts import render, redirect

# Local modules
from patients.models import Patient

# @login_required(login_url='/login/')

def patient_creation(request):
    if request.method == 'POST':
        name = request.POST['name']
        id_type = request.POST['id_type']
        id_number = request.POST['id_number']

        date_birth = request.POST['date_birth']
        age = request.POST['age']
        gender = request.POST['gender']

        civil_state = request.POST['civil_state']
        ocupation = request.POST['ocupation']
        schoolarchip = request.POST['schoolarchip']

        telephone = request.POST['telephone']
        adress = request.POST['adress']
        email = request.POST['email']
        # Create user with the fields above

        patient = Patient.objects.create(name=name, id_type=id_type, id_number=id_number)

        patient.date_birth = request.POST['date_birth']
        patient.age = request.POST['age']
        patient.gender = request.POST['gender']

        patient.civil_state = request.POST['civil_state']
        patient.ocupation = request.POST['ocupation']
        patient.schoolarchip = request.POST['schoolarchip']

        patient.telephone = request.POST['telephone']
        patient.adress = request.POST['adress']
        patient.email = request.POST['email']
        patient.save()
        
        # Redirect to home view
        return redirect('home')
    return render(request,'patient_creation.html')

def patient_profile(request):
    pass