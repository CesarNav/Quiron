""" Modules """
# Djanog modules
from django.shortcuts import render, redirect

# Local modules
from patients.models import Patient
from patients.forms import Patient_Form

# @login_required(login_url='/login/')

def patient_profile(request,id_number):
    #Get the patient by its id_number
    patient = Patient.objects.get(id_number=id_number)
    # Return the patient profile as a dictionary
    return render(request,'patient.html',{'patient':patient})

def patient_creation(request):
    if request.method == 'GET':
        form = Patient_Form()
        context = {
            'form':form
        }
    else:
        form = Patient_Form(request.POST)
        context = {
            'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request,'patient_creation.html', context)

def patient_update(request,id_number):
    patient = Patient.objects.get(id_number=id_number)
    if request.method == 'GET':
        form = Patient_Form(instance=patient)
        print(form)
        context = {
            'form':form
        }
    else:
        form = Patient_Form(request.POST, instance=patient)
        print(form)
        context = {
            'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request,'patient_creation.html',context)