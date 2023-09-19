from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import csv
import os
from django.template.defaulttags import register


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


@register.filter(name='split')
def split(value, key): 
 
    value.split("key")
    return value.split(key)

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
