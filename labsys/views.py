#from labsys.models import Patient
from multiprocessing import context
from django.shortcuts import render, HttpResponse
from .models import *
from django.utils.timezone import datetime 
from django.db.models import Avg, Max, Min, Sum
from .forms import EncounterRegistratioin, PatientRegistration
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
        testid = json.loads(request.body.decode('utf-8'))["testid"]

        ec = Encounter.objects.get(pk=eid)
        chargeItem = ChargeItem.objects.filter(context=ec)
        chargeItem.filter(id=testid).delete()
        
    
        return HttpResponse(status=200)

@login_required(login_url='/login/')
def AddTest(request, e_id, t_id):

        # geting ecnouter object from it's id
        ec = Encounter.objects.get(pk=e_id)
        # geting chargeItemDefination object by it's id
        test = ChargeItemDefinition.objects.get(pk=t_id)
        # creating new ChargeItem object with Chargeitemdefination, Encounter and priceoverride
        new_test = ChargeItem(definitionCanonical=test, context=ec, priceOverride = test.value )
        # Saving new chargeitem object  
        new_test.save()

        return HttpResponseRedirect(reverse("labsys:encounter",  args=[e_id]))

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
        encounter_today = Encounter.objects.filter(timedate__date=datetime.today().date())
        return render(request, 'labsys\index.html', {"encounter" :encounter_today})

    elif request.method == 'POST':
        date = request.POST["date"]
        encounter_date = Encounter.objects.filter(timedate__date=date)
        return render(request, 'labsys\index.html', {"encounter" :encounter_date, "date" : date})


@login_required(login_url='/login/')
def pat_enc(request, pat_id):
    date = "All Encounter for This Patient"
    patient = Patient.objects.get(pk=pat_id)
    encounter = Encounter.objects.filter(patient=patient)
    return render(request, 'labsys\index.html', {"encounter" :encounter, "date" : date})

# renders patient registration form 
@login_required(login_url='/login/')
def patient_regi(request):
    names = Name.objects.all()
    return render(request, 'labsys\patient_regi.html',{ "names": names,
            "form": PatientRegistration   })



        
# get from old patient registration and post from it self 
@login_required(login_url='/login/')
def regi_old_pat(request, pat_id):
    if request.method == "POST":
        form = EncounterRegistratioin(request.POST)
        user = request.user

        if form.is_valid():
            old_patient= Patient.objects.get(pk=pat_id)
            #create new invoice and save without payment details
            inv = Invoice(subject=old_patient, participant = form.cleaned_data["practitioner"], account = form.cleaned_data['account'] )
            inv.save()
            #create new encounter instance
            enc = Encounter()
            # assing it's patient attribute to new_patient instance of Patient Class and save
            enc.patient = old_patient
            enc.practitioner = form.cleaned_data["practitioner"]
            enc.account = form.cleaned_data['account']
            enc.invoice = inv
            enc.save()
            # populate enc instance with queryset test/form.cleaned_data['test'] (as it it diretely populated from object in form) will return queryset as it is foreingkey(many to one)
            enc.test.set(form.cleaned_data["test"])

            # filtering charge items for encounter and getting its subject and enterer filed with patient and user
            chargeItems = ChargeItem.objects.filter(context=enc)
            for c in chargeItems:
                c.subject = old_patient
                c.enterer = request.user
                c.account = form.cleaned_data['account']
                c.save()
            
            p = enc.test.all().aggregate(Sum('value'))
            paid = form.cleaned_data["paid"]
            #populate payment data in invoice object
            inv.discount = form.cleaned_data["discount"]
            inv.totalGross = p['value__sum']
            if not inv.discount:
                inv.discount = 0
            if not paid:
                paid = 0
            inv.totalnet = inv.totalGross - inv.discount
            inv.due = inv.totalnet-paid
            inv.save()

            # next 8 lines implemented for adding priceovcerided field in chage item by default from charge item defination
            price = []
            for p in enc.test.all():
                price.append(p.value)
            test = ChargeItem.objects.filter(context=enc)
            for t in test:
                p = price.pop(0)
                t.priceOverride = p
                t.save()
            #pat_address = Address()
            #pat_address.use = "home"
            #pat_address.text = form.cleaned_data["Address"]
            #pat_address.save()
            if paid:
                payment = PaymentReconciliation(request=inv, paymentAmount= paid, received_by = user)
                payment.save()
            return HttpResponseRedirect(reverse("labsys:index"))
        # if form is not valid
        else:
            return render(request, 'labsys\add_enc.html', {"form": form })
            
    return render(request, 'labsys/add_enc.html', { "pat_id":pat_id, "form": EncounterRegistratioin })

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
            pat_mobile = Telecom(patient=new_patient, system="P", use = "M", value = request.POST["mobile"])
            pat_mobile.save()
            #populate new_telecom instance of Name class for emali
            pat_email = Telecom(patient=new_patient, system="E", use = "W", value = request.POST["email"])
            pat_email.save()
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
            # populate enc instance with queryset test/form.cleaned_data['test'] (as it it diretely populated from object in form) will return queryset as it is foreingkey(many to one)
            enc.test.set(form.cleaned_data["test"])

            # filtering charge items for encounter and getting its subject and enterer filed with patient and user
            chargeItems = ChargeItem.objects.filter(context=enc)
            for c in chargeItems:
                c.subject = new_patient
                c.enterer = request.user
                c.account = form.cleaned_data['account']
                c.save()
            
            p = enc.test.all().aggregate(Sum('value'))
            paid = form.cleaned_data["paid"]
            #populate payment data in invoice object
            inv.discount = form.cleaned_data["discount"]
            inv.totalGross = p['value__sum']
            if not inv.discount:
                inv.discount = 0
            if not paid:
                paid = 0
            inv.totalnet = inv.totalGross - inv.discount
            inv.due = inv.totalnet-paid
            inv.save()

            # next 8 lines implemented for adding priceovcerided field in chage item by default from charge item defination
            price = []
            for p in enc.test.all():
                price.append(p.value)
            test = ChargeItem.objects.filter(context=enc)
            for t in test:
                p = price.pop(0)
                t.priceOverride = p
                t.save()
            #pat_address = Address()
            #pat_address.use = "home"
            #pat_address.text = form.cleaned_data["Address"]
            #pat_address.save()
            if paid:
                payment = PaymentReconciliation(request=inv, paymentAmount= paid, received_by = user)
                payment.save()

            return HttpResponseRedirect(reverse("labsys:index"))
        # if form is not valid
        else:
            return render(request, 'labsys\pat_regi.html', {
                "form": form
            })
    # if request method get      
    return render(request, 'labsys\pat_regi.html', {
            "form": PatientRegistration   })



@login_required(login_url='/login/')
def encounter(request, enc_id):

    e = Encounter.objects.get(pk=enc_id)
    chargeItems = ChargeItem.objects.filter(context= e)
    chargeItem_list = chargeItems.aggregate(Sum('priceOverride'))
    total = chargeItem_list['priceOverride__sum'] or 0

    #Geting invoice object for encouter
    invoice = Invoice.objects.get(pk=e.invoice.id)
    # filtering payment objects for particular invoice
    payments = PaymentReconciliation.objects.filter(request=invoice)
    paymentset = payments.aggregate(Sum('paymentAmount'))
    totalpaid = paymentset['paymentAmount__sum'] or 0
    discount =  invoice.discount or 0
    invoice.totalGross = total
    # checking if no test due to all test deleted and there is discount, totalnet  will be minus 
    if  invoice.totalGross - discount > 0:
        invoice.totalnet = invoice.totalGross - discount
    else:
        invoice.totalnet = 0
    # checking if no test due to all test deleted and there is discount, due will be minus
    if  invoice.totalnet-totalpaid > 0: 
        invoice.due = invoice.totalnet-totalpaid
    else:
        invoice.due = 0
    #saving the invoice
    invoice.save()    

    #creat set of chargeitemdefinations id included in this encounter(allready added tests)
    test_id_set = []
    # list of all chargeitem defination for the encounter
    ChargeItemsDefinition = e.test.all()
    #add chargeitem id to newly created set
    for t in ChargeItemsDefinition:
        test_id_set.append(t.id)
    #creating observationdefination object queryset excluding those in set ie already register  for the encounter
    tests = ChargeItemDefinition.objects.exclude(id__in=test_id_set)

    return render(request, 'labsys\encounter.html', {"e" : e, "chargeItems": chargeItems, "total": total, "payments" : payments, "invoice": invoice, "tests":tests  } )

@login_required(login_url='/login/')
def find(request):
    if request.method == "POST":
        fname = request.POST.get('find_fname')
        lname = request.POST.get("find_lname")
        mobno = request.POST.get("find_mobno")

        if fname and lname and len(fname)>2 and len(lname)>2:
            date=f"Find F Name '{fname}' and L Name '{lname}'"
            name_found = Name.objects.filter(text__icontains=fname).filter(family__icontains=lname)
        elif fname and len(fname)>2:
            if not lname:
                date=f"Find F Name '{fname}'"
                name_found = Name.objects.filter(text__icontains=fname)
            else:
                return render(request,"labsys/find.html",{"message":"Please Search L name by 3 or more characters"}) 
        elif lname and len(lname)>2:
            if not fname:
                date=f"Find L Name '{lname}'"
                name_found = Name.objects.filter(lname__icontains=lname)
            else:
                return render(request,"labsys/find.html",{"message":"Please Search F name by 3 or more characters"})  
        
        elif mobno and len(mobno) == 10 :
            date=f"Find Mobile no '{mobno}'"
            #filtering  telecom objects with particular no as mobile use
            telecoms = Telecom.objects.filter(use="mobile").filter(value=mobno)
            #filtering patient objects with having telecom in filtered telecom set(queryset) telecoms
            if telecoms:
                patients = Patient.objects.filter(telecom__in = telecoms)
                #filtering name objects with having patient in filtered patient set(queryset) patients
                name_found = Name.objects.filter(patient__in=patients)
            else:
                return render(request,"labsys/find.html",{"message":"Patient with such mobilen no not registered"})

        else:
            return render(request,"labsys/find.html",{"message":"Please Search name by 3 or more characters"})
            print("lastloop")
        return render(request, 'labsys/found.html', {"names" : name_found,  "date" : date })
    else:
        return render(request, 'labsys/find.html')

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