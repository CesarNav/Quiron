from django.shortcuts import render, redirect
# Login needed decorator
from django.contrib.auth.decorators import login_required

from reports.forms import Report_Form
from reports.models import Report
from patients.models import Patient

""" Reportlab modules """
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas


@login_required(login_url='/login/')
def report_creation(request):
    #Get the patients list
    patients = Patient.objects.filter(user=request.user,status='A')
    
    if request.method == 'GET':
        form = Report_Form()
        context = {
            'form':form,
            'patients':patients
        }
    else:
        # POST
        form = Report_Form(request.POST)
        context = {
            'form':form,
            'patients':patients
        }
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request,'report_creation.html', context)

@login_required(login_url='/login/')
def report_update(request,id):
    #Get the patients list
    patients = Patient.objects.filter(user=request.user,status='A')

    #Get the report list
    report = Report.objects.get(id = id)
    if request.method == 'GET':
        form = Report_Form(instance=report)
        context = {
            'form':form,
            'patients':patients
        }
    else:
        # POST update instance
        form = Report_Form(request.POST, instance=report)
        context = {
            'form':form,
            'patients':patients
        }
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request,'report_creation.html',context)

@login_required(login_url='/login/')
def report_delete(request,id):
    report = Report.objects.get(id = id)
    report.delete()
  
    return redirect('home')

def report_pdf(request,id_number):
    patient = Patient.objects.get(id_number=id_number)
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(100, 100, 'Hello PDF')

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='Reporte.pdf')

