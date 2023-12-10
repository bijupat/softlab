from django.shortcuts import render, HttpResponse
from django.views.decorators.csrf import csrf_exempt
import csv
import os
from django.template.defaulttags import register
from django.template.loader import get_template
from xhtml2pdf import pisa
from django_xhtml2pdf.utils import pdf_decorator

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
        pass

    return render(request, 'website/book_visit.html')

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
