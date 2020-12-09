from django.shortcuts import render, redirect
# Login needed decorator
from django.contrib.auth.decorators import login_required

from reports.forms import Report_Form
from reports.models import Report


@login_required(login_url='/login/')
def report_creation(request):
    if request.method == 'GET':
        form = Report_Form()
        context = {
            'form':form
        }
    else:
        # POST
        form = Report_Form(request.POST)
        context = {
            'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request,'report_creation.html', context)

@login_required(login_url='/login/')
def report_update(request,id):
    report = Report.objects.get(id = id)
    if request.method == 'GET':
        form = Report_Form(instance=report)
        context = {
            'form':form
        }
    else:
        # POST update instance
        form = Report_Form(request.POST, instance=report)
        context = {
            'form':form
        }
        if form.is_valid():
            form.save()
            return redirect('patient_profile')
    return render(request,'report_creation.html',context)

@login_required(login_url='/login/')
def report_delete(request,id):
    report = Report.objects.get(id = id)
    report.delete()
  
    return redirect('home')

