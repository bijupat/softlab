#from labsys.models import Patient
from django.shortcuts import render, HttpResponse
from .models import *
from django.utils.timezone import datetime 
from django.db.models import Avg, Max, Min, Sum
from .forms import PatientRegistration
from django.http import HttpResponseRedirect
from django.urls import reverse



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

def pat_register(request):
    if request.method == "POST":
        form = PatientRegistration(request.POST, request.FILES)
        user = request.user
        if form.is_valid():
            #print(form.cleaned_data)
            birthdate = form.cleaned_data["birth_date"]
            #pupulate new_patient instance of Patient class
            new_patient = Patient(birthDate=birthdate, gender=request.POST["gender"],  photo=request.FILES['photo'])
            new_patient.save()
            #populate new_name instance of Name class
            pat_name = Name(text=request.POST["f_name"], patient=new_patient, family=request.POST["l_name"] )
            pat_name.save()
            #populate new_tele instance of Name class
            pat_telecom = Telecom(patient=new_patient, system="phone", use = "mobile", value = request.POST["mobile"])
            pat_telecom.save()
            #create new encounter instance
            enc = Encounter()
            # assing it's patient attribute to new_patient instance of Patient Class and save
            enc.patient = new_patient
            enc.practitioner = form.cleaned_data["practitioner"]
            enc.account = form.cleaned_data['account']
            enc.save()
            # populate enc instance with queryset test/form.cleaned_data['test'] will return queryset as it is foreingkey(many to one)
            enc.test.set(form.cleaned_data["test"])
            
            #pat_address = Address()
            #pat_address.use = "home"
            #pat_address.text = form.cleaned_data["Address"]
            #pat_address.save()
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, 'labsys\pat_regi.html', {
                "form": form
            })
    else:

     

        return render(request, 'labsys\pat_regi.html', {
            "form": PatientRegistration   })



def encounter(request, enc_id):
    e = Encounter.objects.get(pk=enc_id)
    p = e.test.all().aggregate(Sum('price'))
    total = p['price__sum']

    return render(request, 'labsys\encounter.html', {"e" : e, "total": total})