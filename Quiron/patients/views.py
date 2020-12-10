""" Django Modules """
# Djanog modules
from django.shortcuts import render, redirect
# Login needed decorator
from django.contrib.auth.decorators import login_required

""" Local modules """
from patients.models import Patient
from reports.models import Report
from patients.forms import Patient_Form

@login_required(login_url='/login/')
def patient_profile(request,id_number):
    #Get the patient by its id_number
    patient = Patient.objects.get(id_number=id_number)

    #Get the patients list
    patients = Patient.objects.filter(user=request.user,status='A')

    reports = Report.objects.filter(patient_id=id_number)

    context = {
        'patient':patient,
        'reports':reports,
        'patients':patients,
    }
    # Return the patient profile as a dictionary
    return render(request,'patient.html', context)

@login_required(login_url='/login/')
def patient_creation(request):

    #Get the patients list
    patients = Patient.objects.filter(user=request.user,status='A')

    if request.method == 'GET':
        form = Patient_Form()
        context = {
            'form':form,
            'patients':patients,
        }
    else:
        # POST
        form = Patient_Form(request.POST)
        context = {
            'form':form,
            'patients':patients,
        }
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request,'patient_creation.html', context)

@login_required(login_url='/login/')
def patient_update(request,id_number):

    #Get the patients list
    patients = Patient.objects.filter(user=request.user,status='A')

    patient = Patient.objects.get(id_number=id_number)
    if request.method == 'GET':
        form = Patient_Form(instance=patient)
        context = {
            'form':form,
            'patients':patients,
        }
    else:
        # POST update instance
        form = Patient_Form(request.POST, instance=patient)
        context = {
            'form':form,
            'patients':patients,
        }
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request,'patient_creation.html',context)

@login_required(login_url='/login/')
def patient_deactivate(request,id_number):
    patient = Patient.objects.get(id_number=id_number)
    patient.status = "D"
    patient.save()
    return redirect('home')

@login_required(login_url='/login/')
def patient_delete(request,id_number):
    patient = Patient.objects.get(id_number=id_number)
    patient.delete()
  
    return redirect('home')