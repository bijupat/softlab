#from labsys.models import Patient
from django.shortcuts import render, HttpResponse
from .models import *
from django.utils.timezone import datetime 
from django.db.models import Avg, Max, Min, Sum

# Create your views here.


def index(request):
    if request.method == 'GET':
        #date format (yyyy,mm,dd)
        encounter_today = Encounter.objects.filter(timedate__date=datetime.today().date())

        """
        encounter_date = Encounter.objects.filter(timedate__date=datetime(2021, 6, 2).date())
        print(encounter_today)
        for e in encounter_today:
            #e.test.all().(total=sum('price'))
            p = e.test.all().aggregate(Sum('price'))
            print(p)
        #create empty list to pass to template as value dic
        context = []
        for e in encounter_today:
            #create dic item for each encounter
            object = {}
            #add value to object dict with different key 
            object["date"] = e.timedate.date()
            object["patient"] = e.patient.patient_name.get().text +" "+ e.patient.patient_name.get().family
            object["id"] = e.id
            object["practitioner"] = e.practitioner
            object["account"] = e.account
            object["test"] = e.test.all()
            

            #add object dict to list context
            context.append(object)
        print(context)
        """
        return render(request, 'labsys\index.html', {"encounter" :encounter_today})
    elif request.method == 'POST':
        
        encounter_date = Encounter.objects.filter(timedate__date=datetime.today().date())

        return render(request, 'labsys\index.html', {"encounter" :encounter_date})




def encounter(request, enc_id):
    e = Encounter.objects.get(pk=enc_id)
    p = e.test.all().aggregate(Sum('price'))
    total = p['price__sum']

    return render(request, 'labsys\encounter.html', {"e" : e, "total": total})