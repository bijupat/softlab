from django.shortcuts import render, HttpResponse
#from django.views.decorators.csrf import csrf_exempt
import csv, requests, os
#import os
from django.template.defaulttags import register
from django.template.loader import get_template
from xhtml2pdf import pisa
from django_xhtml2pdf.utils import pdf_decorator
from .forms import  PatientRegistration
#from django.http import HttpResponseRedirect
#from django.urls import reverse
from .models import Patient, Appointment
from django.contrib.auth.decorators import login_required

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#register filter for template
@register.filter(name='split')
def split(value, key): 
    value.split("key")
    return value.split(key)



@pdf_decorator(pdfname='Mahi Pricelist.pdf')
def pricelistview(request):
    if request.method == "POST":
        pass    
    context = []
    with open(os.path.join(BASE_DIR,'pricelist.csv')) as file:
        reader = csv.DictReader(file)
        for row in reader:
            context.append(row)
    return render(request, 'website/pricelist.html', {'context' : context})


def profilespreview(request):
    context = []
    with open(os.path.join(BASE_DIR,'profiles.csv')) as file:
        reader = csv.DictReader(file)
        for row in reader:
            context.append(row)
    template_path = 'website/profileview.html'
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf') 


    # if dawnload 
    #response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # if display 
    response['Content-Disposition'] = f'filename="Mahi Diagnostics Profiles.pdf"'

    # find the template and render it.
    template = get_template(template_path)
    html = template.render({'context': context})

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
# Create your views here.
def index(request):
    
    return render(request, 'website/index.html')


#@csrf_exempt
def get_price(request):
    if request.method == "POST":
        pass    
    context = []
    with open(os.path.join(BASE_DIR,'pricelist.csv')) as file:
        reader = csv.DictReader(file)
        for row in reader:
            context.append(row)
    return render(request, 'website/get_price.html', {'context' : context})


#@pdf_decorator(pdfname='new_filename.pdf')
def profiles(request):
    if request.method == "POST":
        pass 
    context = []
    with open(os.path.join(BASE_DIR,'profiles.csv')) as file:
        reader = csv.DictReader(file)
        for row in reader:
            context.append(row)
    return render(request, 'website/profiles.html', {'context' : context})

def book_visit(request):
    if request.method == "POST":
        form = PatientRegistration(request.POST)
        if form.is_valid():
            fname = form.cleaned_data["f_name"].title()
            mname = form.cleaned_data["m_name"].title()
            lname = form.cleaned_data["l_name"].title()
            gender = form.cleaned_data["gender"]
            birth_date = form.cleaned_data["birth_date"]
            mobile = form.cleaned_data["mobile"]
            email = form.cleaned_data["email"].lower()
            visit_time = form.cleaned_data["visit_time"]
            tests = form.cleaned_data["tests"].title()
            address = form.cleaned_data["address"].title()
            new_patient = Patient(f_name = fname, m_name = mname, l_name = lname, mobile = mobile, email = email, gender = gender,  birthDate = birth_date , address = address )
            new_patient.save()
            new_appointment = Appointment(time = visit_time, subject = new_patient, tests = tests )
            new_appointment.save()
            SMSText = f"Respected {fname} {lname}, Your Appointment on {visit_time} for blood tests {tests} is booked. Address: {address} Call 7016944046 if any query MEDI LAB"
            #SMSText = f"Patient Name: {fname} {lname} Ref No: {visit_time} Reports is: {tests} Call: {mobile} For Any Query Contact,MEDILAB DIAGNOSTIC"
            url_pat = f"https://onlysms.co.in/api/sms.aspx?UserID=MediLB&UserPass=Gurudev@101&MobileNo=91{mobile}&GSMID=MEDIDC&PEID=1301161848129500767&Message={SMSText}&UNICODE=TEXT"            
            url_lab = f"https://onlysms.co.in/api/sms.aspx?UserID=MediLB&UserPass=Gurudev@101&MobileNo=919909016867&GSMID=MEDIDC&PEID=1301161848129500767&Message={SMSText}&UNICODE=TEXT"            
            print(SMSText)
            print(url_lab)
            responce = requests.get(url_lab) 
            print(responce.status_code)
            print(responce.text)
            return render(request, 'website/thankyou.html',{"patient": form.cleaned_data,})
        # if form is not valid
        else:
            return render(request, 'website/book_visit.html', {"form": form, "message":form.errors })   
    # if request method get
    return render(request, 'website/book_visit.html',{ "form": PatientRegistration, })

@login_required(login_url='/lab/login/')
def manage_visit(request):
    if request.method == "POST":
        pass
    
    appointments  = Appointment.objects.all()
    return render(request, 'website/view_visit.html',{"appointments": appointments})

def contactus(request):
    if request.method == "POST":
        pass
    
    return render(request, 'website/contactus.html')

def aboutus(request):
    if request.method == "POST":
        pass

    return render(request, 'website/aboutus.html')

def privacy(request):
    if request.method == "POST":
        pass

    return render(request, 'website/privacy.html')

def camp(request):
    if request.method == "POST":
        pass

    return render(request, 'website/camp.html')

def termsconditions(request):
    if request.method == "POST":
        pass

    return render(request, 'website/termsconditions.html')
