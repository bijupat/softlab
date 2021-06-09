from labsys.models import Patient
from django.shortcuts import render, HttpResponse
from .models import *
from django.utils.timezone import datetime 

# Create your views here.


def index(request):
    #date format (yyyy,mm,dd)
    encounter_today = Encounter.objects.filter(timedate__date=datetime.today().date())
    encounter_date = Encounter.objects.filter(timedate__date=datetime(2021, 6, 2).date())
    print(encounter_today)
    context = {}
    i=0
    for e in encounter_today:
        object = {}
        object["date"] = e.timedate.date()
        object["pat_name"] = e.patient.patient_name.get().text +" "+ e.patient.patient_name.get().family
        context[i] = object
        i=i+1
    print(context)
    print(context[1].date)
    return render(request, 'labsys\index.html', context)

