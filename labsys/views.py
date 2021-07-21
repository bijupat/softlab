#from labsys.models import Patient
from django.shortcuts import render, HttpResponse
from .models import *
from django.utils.timezone import datetime 
from django.db.models import Avg, Max, Min, Sum
from .forms import PatientRegistration
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView

class InvoiceListView(ListView):
    model = Invoice
    context_object_name = 'invoice_Obj'


def AddPayment(request):
    form = PatientRegistration(request.POST, request.FILES)
    user = request.user
    
    if request.method == 'GET':

        return render(request, 'labsys\payment.html')


    if request.method == 'POST':

        return HttpResponseRedirect(reverse("encounter", args=[5]))


def index(request):
    if request.method == 'GET':
        #date format (yyyy,mm,dd)
        encounter_today = Encounter.objects.filter(timedate__date=datetime.today().date())

        return render(request, 'labsys\index.html', {"encounter" :encounter_today})

    elif request.method == 'POST':
        date = request.POST["date"]
        encounter_date = Encounter.objects.filter(timedate__date=date)

        return render(request, 'labsys\index.html', {"encounter" :encounter_date, "date" : date})

def pat_register(request):
    if request.method == "POST":
        form = PatientRegistration(request.POST, request.FILES)
        user = request.user
        if form.is_valid():
            #print(form.cleaned_data)
            #pupulate new_patient instance of Patient class
            new_patient = Patient(birthDate=form.cleaned_data["birth_date"], gender=request.POST["gender"],  photo=request.FILES['photo'])
            new_patient.save()
            #populate new_name instance of Name class
            pat_name = Name(text=request.POST["f_name"].title(), patient=new_patient, family=request.POST["l_name"].title() )
            pat_name.save()
            #populate new_tele instance of Name class
            pat_telecom = Telecom(patient=new_patient, system="phone", use = "mobile", value = request.POST["mobile"])
            pat_telecom.save()
            #create new invoice and save without payment details
            inv = Invoice(subject=new_patient, participant = form.cleaned_data["practitioner"], account = form.cleaned_data['account'] )
            inv.save()
            #create new encounter instance
            enc = Encounter()
            # assing it's patient attribute to new_patient instance of Patient Class and save
            enc.patient = new_patient
            enc.practitioner = form.cleaned_data["practitioner"]
            enc.account = form.cleaned_data['account']
            enc.invoice = inv
            enc.save()
            # populate enc instance with queryset test/form.cleaned_data['test'] will return queryset as it is foreingkey(many to one)
            enc.test.set(form.cleaned_data["test"])
            p = enc.test.all().aggregate(Sum('price'))
            paid = form.cleaned_data["paid"]
            #populate payment data in invoice object
            inv.discount = form.cleaned_data["discount"]
            inv.totalGross = p['price__sum']
            inv.totalnet = inv.totalGross - inv.discount
            inv.due = inv.totalnet-paid
            inv.save()
       
            
            #pat_address = Address()
            #pat_address.use = "home"
            #pat_address.text = form.cleaned_data["Address"]
            #pat_address.save()

            payment = PaymentReconciliation(request=inv, paymentAmount= paid)
            payment.save()

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

