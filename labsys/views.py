#from labsys.models import Patient
from django.shortcuts import render, HttpResponse
from .models import *
from django.utils.timezone import datetime 
from django.db.models import Avg, Max, Min, Sum
from .forms import PatientRegistration
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required


class InvoiceListView(ListView):
    model = Invoice
    context_object_name = 'invoice_Obj'


@csrf_exempt
@login_required(login_url='/login/')
def DeleteTest(request):
    if request.method == "POST":
        eid = json.loads(request.body.decode('utf-8'))["eid"]
        test = json.loads(request.body.decode('utf-8'))["test"]

        ec = Encounter.objects.get(pk=eid)
        ob = Observation.objects.filter(encounter=ec)
        ob.filter(test_id=test).delete()
        
    
        return HttpResponse(status=200)

@login_required(login_url='/login/')
def AddTest(request):
    if request.method == "POST":
        
        eid = request.POST["eidinput"]
        testid = request.POST["addtest"]
        ec = Encounter.objects.get(pk=eid)
        test = ObservationDefinition.objects.get(pk=testid)
        new_test = Observation(test=test, encounter=ec)
        new_test.save()
        #print(eid)
        #print(testid)
        return HttpResponseRedirect(reverse("labsys:encounter",  args=[eid]))

@login_required(login_url='/login/')
def AddEditDiscount(request):
    if request.method == "POST":
        eid = request.POST["eidinput"]
        discount = request.POST["addeditdiscountinput"]
        ec = Encounter.objects.get(pk=eid)
        invoice = ec.invoice
        invoice.discount = discount        
        invoice.save()
        #print(eid)
        #print(discount)
        return HttpResponseRedirect(reverse("labsys:encounter",  args=[eid]))

@login_required(login_url='/login/')
def AddPayment(request):
    form = PatientRegistration(request.POST, request.FILES)
    user = request.user
    
    if request.method == 'GET':

        return render(request, 'labsys\payment.html')


    if request.method == 'POST':

        return HttpResponseRedirect(reverse("labsys:encounter", args=[5]))

@login_required(login_url='/login/')
def index(request):
    if request.method == 'GET':
        #date format (yyyy,mm,dd)
        encounter_today = Encounter.objects.filter(timedate__date=datetime.today().date())

        return render(request, 'labsys\index.html', {"encounter" :encounter_today})

    elif request.method == 'POST':
        date = request.POST["date"]
        encounter_date = Encounter.objects.filter(timedate__date=date)

        return render(request, 'labsys\index.html', {"encounter" :encounter_date, "date" : date})
        
@login_required(login_url='/login/')
def pat_register(request):
    if request.method == "POST":
        form = PatientRegistration(request.POST, request.FILES)
        user = request.user
        if form.is_valid():
            #print(form.cleaned_data)
            #pupulate new_patient instance of Patient class
            new_patient = Patient(birthDate=form.cleaned_data["birth_date"], gender=form.cleaned_data["gender"],  photo=form.cleaned_data['photo'])
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
            if not inv.discount:
                inv.discount = 0
            if not paid:
                paid = 0
            inv.totalnet = inv.totalGross - inv.discount
            inv.due = inv.totalnet-paid
            inv.save()
       
            
            #pat_address = Address()
            #pat_address.use = "home"
            #pat_address.text = form.cleaned_data["Address"]
            #pat_address.save()
            if paid:
                payment = PaymentReconciliation(request=inv, paymentAmount= paid, received_by = user)
                payment.save()

            return HttpResponseRedirect(reverse("labsys:index"))
        else:
            return render(request, 'labsys\pat_regi.html', {
                "form": form
            })
    else:

     

        return render(request, 'labsys\pat_regi.html', {
            "form": PatientRegistration   })


@login_required(login_url='/login/')
def encounter(request, enc_id):
    e = Encounter.objects.get(pk=enc_id)
    p = e.test.all().aggregate(Sum('price'))
    total = p['price__sum']
    invoice = Invoice.objects.get(pk=e.invoice.id)
    payments = PaymentReconciliation.objects.filter(request=invoice)
    paymentset = payments.aggregate(Sum('paymentAmount'))
    totalpaid = paymentset['paymentAmount__sum']
    discount =  invoice.discount
    invoice.totalGross = total
    if discount:
        invoice.totalnet = invoice.totalGross - discount
    else:
        invoice.totalnet = invoice.totalGross
    if totalpaid:
        invoice.due = invoice.totalnet-totalpaid
    else:
        invoice.due = invoice.totalnet
    invoice.save()
    tests = ObservationDefinition.objects.all()
    
    #creat set of observationdefination id included in this encounter(allready added tests)
    test_id_set = []
    #add observationdefination id to newly created set
    for t in e.test.all():
        test_id_set.append(t.id)
    #creating observationdefination object queryset excluding those in set
    tests = ObservationDefinition.objects.exclude(id__in=test_id_set)

    return render(request, 'labsys\encounter.html', {"e" : e, "total": total, "payments" : payments, "invoice": invoice, "tests":tests  } )

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("labsys:index"))
        else:
            return render(request, "labsys/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "labsys/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("labsys:index"))

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "labsys/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "labsys/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("labsys:index"))
    else:
        return render(request, "labsys/register.html")