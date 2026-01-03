#from labsys.models import Patient
#from multiprocessing import context
from django.shortcuts import render, HttpResponse, get_object_or_404
from .models import *
from django.http import JsonResponse, FileResponse, HttpResponseRedirect
from django.utils.timezone import datetime 
from .forms import PatientRegistration, AppointmentRegistration, RequestRegi_1, RequestRegi_2
from django.urls import reverse
from django.views.generic import ListView
from django.views.decorators.csrf import csrf_exempt
import json
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError, connection
from django.contrib.auth.decorators import login_required
from reportlab.pdfgen import canvas
import io
from django.template.loader import get_template
from xhtml2pdf import pisa
from django import forms
from pprint import pprint
from django.utils.datastructures import MultiValueDictKeyError
from django.db.models import Count, F, Value


@login_required(login_url='/lab/login/')
def ChargeitemDataEdit(request,ci_id):
    if request.method == "POST":
        chargeitem  = ChargeItem.objects.get(pk=ci_id)
        chargeitem.priceOverride = request.POST["priceOverride"]
        chargeitem.overrideReason = request.POST["overrideReason"]
        chargeitem.note = request.POST["note"]
        chargeitem.priceoverrideby = request.user
        chargeitem.save()
        return HttpResponseRedirect(reverse("labsys:encounter",  args=[chargeitem.context.id]))
    else:
        chargeItem = ChargeItem.objects.get(pk=ci_id)
        return render(request, 'labsys/chargeitemdataedit.html', {"chargeItem" :chargeItem})

@login_required(login_url='/lab/login/')
def ObservationDataEdit(request,ob_id):
    if request.method == "POST":
        observation  = Observation.objects.get(pk=ob_id)
        observation.unit = request.POST["unit"]
        observation.high = request.POST["high"]
        observation.low = request.POST["low"]
        observation.note = request.POST["note"]
        observation.save()
        return HttpResponseRedirect(reverse("labsys:chargeitem",  args=[observation.chargeitem.id, "edit"]))
    else:
        observation = Observation.objects.get(pk=ob_id)
        return render(request, 'labsys/observationdataedit.html', {"observation" :observation})



@login_required(login_url='/lab/login/')
def chargeitem_preview(request, *args, **kwargs):
    pk = kwargs.get('pk')
    chargeitem = get_object_or_404(ChargeItem, pk=pk) 
    # reverse query by related name "observation" 
    observations = chargeitem.observation.all()
    # observations = Observation.objects.filter(chargeitem=chargeitem)
    is_all_ob_entered = True
    is_all_ob_final_or_above = True
    obs = {}

    for ob in observations:
        #checking if ob.value is not than set variable to false, even single observation is not set it will turn to False
        if not ob.value:
            is_all_ob_entered = False
        #checking if ob.status is either P or R set variable to false, even single observation is not set it will turn to False
        if ob.status == "P" or ob.status == "R":
            is_all_ob_final_or_above = False
        print("status check")
        # itereting over all chargeitemdefinations associated with observationdef(testfield)
        print(ob.testfield)
        # print(ob.testfield.chargeitemdef.all())
        for cdef in ob.testfield.chargeitemdef.all():
            # if present chargeitem is profile
            # if False:
            if chargeitem.definitionCanonical.is_profile:
                # if iterating chargeitem(cdef) is not included in profile (present) chargeitem
                # print(chargeitem.definitionCanonical.includes.all())
                # print(cdef)
                if cdef not in chargeitem.definitionCanonical.includes.all():
                    # if key not present in obs dict create new key with present chargeitem heading
                    if chargeitem.definitionCanonical.heading not in obs:
                        obs[chargeitem.definitionCanonical.heading] = [ob]
                        # print(obs)
                    # if key is present append it with the observation
                    elif ob not in obs[chargeitem.definitionCanonical.heading]:
                        obs[chargeitem.definitionCanonical.heading].append(ob)
                        # print(obs)        
                # else (iterating chargeitem(cdef) is included in profile (present) chargeitem)
                # in this case we provide same heading as the included chargeitem
                # ie if CBC chargeitemdef is included in PREOP chargeitemdef for observations in CBC heading (key) will be as per CBC chargeitemdef heading
                else:
                    if cdef.heading not in obs:
                        obs[cdef.heading] = [ob]
                    elif ob not in obs[cdef.heading]:
                        obs[cdef.heading].append(ob)
            # else (present charegeitem is not profile)
            else:
                # if itereting chargeitem cdef is not same as present charegeitem
                if cdef == chargeitem.definitionCanonical:
                    # if key not present in obs dict create new key with present chargeitem heading
                    if cdef.heading not in obs:
                        obs[cdef.heading] = [ob]
                    # if key is present append it with the observation
                    elif ob not in obs[cdef.heading]:
                        obs[cdef.heading].append(ob)
                
        # if all observation not final or above return to encounter:  for server side validation
    if not is_all_ob_final_or_above or len(observations) == 0:
        return HttpResponseRedirect(reverse("labsys:encounter", args=[chargeitem.context.id]))
    # for heading, observations in obs.items():
    #     print(heading)
    #     for observation in observations:
    #         print (observation.value)    
    context =  {"observations": obs, "chargeitem" : chargeitem, "is_all_ob_entered":is_all_ob_entered, "is_all_ob_final_or_above": is_all_ob_final_or_above} 

    template_path = 'labsys/obs_by_chgItm_preview.html'
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf') 


    # if dawnload 
    #response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # if display 
    response['Content-Disposition'] = f'filename="{chargeitem.subject.get_usual_name()} ({chargeitem.context.id}).pdf"'

    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

@login_required(login_url='/lab/login/')
def chargeitem_preview2(request):
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer)

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    template_path = 'labsys/obs_by_chgItm_preview.html'
    context = {'client': "c"}
    template = get_template(template_path)
    html = template.render(context)

    p.drawString(50, 800, html)

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer,  filename='hello.pdf')

class InvoiceListView(ListView):
    model = Invoice
    context_object_name = 'invoice_Obj'

@csrf_exempt
@login_required(login_url='/lab/login/')
def search(request):
    fname = json.loads(request.body.decode('utf-8'))["fname"]
    lname = json.loads(request.body.decode('utf-8'))["lname"]
    mobno = json.loads(request.body.decode('utf-8'))["mobno"]

    if len(mobno) == 10:
        telecoms = Telecom.objects.filter(use="M").filter(value=mobno)
        patients = Patient.objects.filter(telecom__in = telecoms)
        #filtering name objects with having patient in filtered patient set(queryset) patients
        name_found = Name.objects.filter(patient__in=patients)
        names = name_found.order_by("-text").all()
        return JsonResponse([name.serialize() for name in names], safe=False)
    else:
        if fname and lname:
            name_found = Name.objects.filter(given__icontains=fname).filter(family__icontains=lname)
            names = name_found.order_by("-given").all()
            return JsonResponse([name.serialize() for name in names], safe=False)
        if fname and not lname:
            name_found = Name.objects.filter(given__icontains=fname)
            names = name_found.order_by("-given").all()
            return JsonResponse([name.serialize() for name in names], safe=False)
        if lname and not fname:
            name_found = Name.objects.filter(family__icontains=lname)
            names = name_found.order_by("-given").all()
            return JsonResponse([name.serialize() for name in names], safe=False)
        
    return HttpResponse(status=400)


#@@@ CONSIDER PREFETCH_RELATED OR SELECT_RELATED FOR THIS VIEW TO FETCH PATIENT WITH SEARCH OF NAME/TELCOMS
@login_required(login_url='/lab/login/')
def hx_patient_search(request):
    # print(request.POST)
    if request.method == 'POST':
        try:
            mobile = request.POST['mobile']
            if len(mobile)==10:
                # this query create innerjoin on name, patient and telecom models in single query
                names = Name.objects.select_related('content_type').filter(patient__telecoms__use="M", patient__telecoms__value = mobile)
                message = f"Search result of Mobile no : '{mobile}'"
                return render(request, 'labsys/hx_patients.html', {"names" :names, "message" : message})
            else:
                return HttpResponse("<h4 style='color:red' class = 'text-center'>Please enter valid 10 digit mobile Number</h4>")
        except MultiValueDictKeyError:
            fname = request.POST["fname"]
            lname = request.POST["lname"]
            if len(fname) > 2 and len(lname)> 2:
                names = Name.objects.select_related('content_type').filter(given__icontains=fname, family__icontains=lname, content_type__model = 'patient' )
                message = f"Search result of First name : '{fname}' and Last name : '{lname}'"
                return render(request, 'labsys/hx_patients.html', {"names" :names, "message" : message})
            if len(fname) > 2:
                message = f"Search result of First name : '{fname}'"
                names = Name.objects.filter(given__icontains=fname).exclude(patient=None)
                return render(request, 'labsys/hx_patients.html', {"names" :names, "message" : message})
            if len(lname) > 2:
                message = f"Search result of Last Name : '{lname}'"
                names = Name.objects.filter(family__icontains=lname).exclude(patient=None)
                return render(request, 'labsys/hx_patients.html', {"names" :names, "message" : message})
            return HttpResponse("<h4 style='color:red'class = 'text-center'>Please enter atleast three letters</h4>")
    return render(request, 'labsys/patient_search.html')

@login_required(login_url='/lab/login/')
def add_request_1(request, **kwargs):
    if request.method == "POST":
        form = RequestRegi_1(request.POST)
        if form.is_valid():
            practitioner = form.cleaned_data["practitioner"]
            account = form.cleaned_data["account"]
            pricelist = account.pricelist
            # print(account)
            # print(practitioner)
        form = RequestRegi_2()
        # add test field in form modelform
        # form.fields['test'].queryset = ChargeItemDefinition.objects.filter(price__pricelist = "3", status = "a")  
        form.fields['tests'] = forms.ModelMultipleChoiceField(queryset=ChargeItemDefinition.objects.filter(price_s__pricelist = pricelist , status = "A"),required=False,label = "Tests", widget=forms.SelectMultiple(attrs={'class': 'form-control chosen-select'}))

        # form.fields['test'].queryset = ChargeItemDefinition.objects.filter(pricelist_included = 1)
        return render(request, 'labsys/add_request_2.html', { "pat_id": kwargs['pat_id'], "form": form, "pract_id":practitioner.id , "plist_id":pricelist.id })
    
    else:
        form = RequestRegi_1()
        # pratitioners = Practitioner.objects.prefetch_related("names")
        # form.fields['practitioner'].queryset = pratitioners
        return render(request, 'labsys/add_request_1.html', {"pat_id" :kwargs['pat_id'], "form" : form})


@login_required(login_url='/lab/login/')
def add_request_2(request, **kwargs):
    if request.method == "POST":
        form = RequestRegi_2(request.POST)
        if form.is_valid():
            ser_req = ServiceRequet(subject = get_object_or_404( Patient, pk = kwargs['pat_id']), 
                                    practitioner = get_object_or_404(Practitioner, pk = kwargs['pract_id']), 
                                    account = get_object_or_404(Account , pk = kwargs['plist_id']),
                                    status ="A",
                                    category = 'L',
                                    priority = 'R',
                                    requester = request.user,
                                    authoredOn = form.cleaned_data["appointment_time"]
                                    )
            ser_req.save()
            tests = form.cleaned_data["tests"]
            specimentype = set()
            for test in tests:
                for s in test.specimentypes.all():
                    specimentype.add(s.id)
            ser_req.tests.set(tests)
            ser_req.specimentypes.set(specimentype)           
            return HttpResponseRedirect(reverse("labsys:service-requests"))
        
        else:
            return render(request, 'labsys/add_request_2.html', { "pat_id": kwargs['pat_id'], 
                                                                 "form": form,
                                                                 "pract_id":kwargs['pract_id'],
                                                                 "plist_id":kwargs['plist_id'] })

@login_required(login_url='/lab/login/')
def add_encounter(request, **kwargs):
    ser_req_id = kwargs['req_id']
    req = ServiceRequet.objects.annotate(fname = F("subject__names__text")).get(pk=ser_req_id)
    
    return render(request, 'labsys/add_encounter.html', {"req" :req })

@login_required(login_url='/lab/login/')
def servicerequests(request):
    if request.method == "POST":
        pass
        
    servicerequests = ServiceRequet.objects.select_related("subject",
                                                           "practitioner",
                                        ).prefetch_related("subject__names",
                                                             "tests", 
                                                             "specimentypes",
                                                             "requester",
                                                             "practitioner__names",
                                                             "account"
                                        ).annotate(fname = F("subject__names__text"))
    
    return render(request, 'labsys/view_requests.html',{'requests' :servicerequests})

@csrf_exempt
@login_required(login_url='/lab/login/')
def DeleteTest(request):
    if request.method == "POST":
        # eid = json.loads(request.body.decode('utf-8'))["eid"]
        testid = json.loads(request.body.decode('utf-8'))["testid"]
        # invoice = Encounter.objects.get(pk=eid).invoice
        chargeitem = ChargeItem.objects.get(pk=testid)
        Observation.objects.filter(chargeitem = chargeitem).delete()
        chargeitem.delete()
        return HttpResponse(status=200)

@login_required(login_url='/lab/login/')
def AddTest(request, e_id, t_id):    
        # geting ecnouter object from it's id
        enc = Encounter.objects.get(pk=e_id)
        # geting chargeItemDefination object by it's id
        test = ChargeItemDefinition.objects.get(pk=t_id)        
        # creating new ChargeItem object with Chargeitemdefination, Encounter and priceoverride
        new_test = ChargeItem(definitionCanonical=test, context=enc, subject=enc.patient, enterer=request.user, account = enc.account)        
        # Saving new chargeitem object without priceOverride as it is tobe obtained from class method update_price
        new_test.save()
        new_test.update_price()
        new_test.save()      
        #finding set of observationdefs under test(chargeitemdef)
        obs = test.observations.all()
        # adding filtered observationdef to chageitem.observation(new_test.observation) as set
        new_test.observations.set(obs)
        # adding observations from included charge items
        included_tests = test.includes.all()
        for t in included_tests:
            for o in t.observations.all():
                new_test.observations.add(o)
        # add default values to observatioin from ob_def    
        observations = Observation.objects.filter(chargeitem = new_test)
        for o in observations:
            # calss method pupulate_fm_obdef copies normal and other default values
            o.populate_fm_obdef()
        return HttpResponseRedirect(reverse("labsys:encounter",  args=[e_id]))

@login_required(login_url='/lab/login/')
def AddEditDiscount(request):
    if request.method == "POST":
        invoice = Encounter.objects.get(pk=request.POST["eidinput"]).invoice
        invoice.discount = request.POST["addeditdiscountinput"]        
        invoice.save()
        return HttpResponseRedirect(reverse("labsys:encounter",  args=[request.POST["eidinput"]]))

@login_required(login_url='/lab/login/')
def ObservationEdit(request):
    if request.method == "POST": 
        chargeitem = ChargeItem.objects.get(pk=request.POST["chargeitem_id"])  
        # reverse query by related name "observation" 
        observations = chargeitem.observation.all()  
        # observations = Observation.objects.filter(chargeitem=chargeitem)        
        for ob in observations:
            try:
                if request.POST[str(ob.id)]:
                    ob.value = request.POST[str(ob.id)]
                    ob.status = "P"
                    ob.prelimnary_by = request.user
                    ob.prelimnary_timedate = datetime.now()
                    ob.save()
            except:
                pass
        return HttpResponseRedirect(reverse("labsys:chargeitem",  args=[request.POST["chargeitem_id"], "view"]))
  

@login_required(login_url='/lab/login/')
def ObservationVerifyAll(request):
    if request.method == "POST": 
        chargeitem_id = request.POST["chargeitem_id"]    
        chargeitem = ChargeItem.objects.get(pk=chargeitem_id)
        # reverse query by related name "observation" 
        observations = chargeitem.observation.all()    
        # observations = Observation.objects.filter(chargeitem=chargeitem)
        
        for ob in observations:
                ob.status = "F"
                ob.final_by = request.user
                ob.final_timedate = datetime.now()
                ob.save()
            
        return HttpResponseRedirect(reverse("labsys:chargeitem",  args=[chargeitem_id, "view"]))

@login_required(login_url='/lab/login/')
def ObservationVerify(request, ob_id):
    
    observation = Observation.objects.get(pk=ob_id)
    chagreitem_id = observation.chargeitem.id
    observation.status = "F"
    observation.final_by = request.user
    observation.final_timedate = datetime.now()
    observation.save()

        
    return HttpResponseRedirect(reverse("labsys:chargeitem",  args=[chagreitem_id, "edit"]))


@login_required(login_url='/lab/login/')
def AddPayment(request):
    if request.method == 'POST':
        eid = request.POST["eidinput"]
        ec = Encounter.objects.get(pk=eid)
        invoice = ec.invoice
        payment = PaymentReconciliation(request=invoice, received_by=request.user,
                    paymentAmount=request.POST["payamount"])
        payment.save()
        return HttpResponseRedirect(reverse("labsys:encounter", args=[eid]))
            
    return render(request, 'labsys/h_filter.html')


@login_required(login_url='/lab/login/')
def index(request):
    if request.method == 'POST':
        date = request.POST["date"]
        encounter_date = Encounter.objects.filter(timedate__date=date)
        return render(request, 'labsys/index.html', {"encounter" :encounter_date, "date" : date})
    #if request method is get
    encounter_today = Encounter.objects.filter(timedate__date=datetime.today().date())
    return render(request, 'labsys/index.html', {"encounter" :encounter_today})

        



@login_required(login_url='/lab/login/')
def regi_appointment(request, pat_id):
    if request.method == "POST":
        form = AppointmentRegistration(request.POST)
        if form.is_valid():
            new_appointment = Appointment()
            new_appointment.priority = form.cleaned_data["priority"]
            new_appointment.description = form.cleaned_data["description"]
            new_appointment.start = form.cleaned_data["start"]
            new_appointment.end = form.cleaned_data["end"]
            new_appointment.slot = form.cleaned_data["slot"]
            new_appointment.account = form.cleaned_data["account"]
            new_appointment.created = datetime.now()
            new_appointment.created_by = request.user
            new_appointment.patientinstruction = form.cleaned_data["patientinstruction"]
            new_appointment.subject = Patient.objects.get(pk=pat_id)
            new_appointment.organization = form.cleaned_data["organization"]
            try:
                new_appointment.save()
                # new appointment need to saved as needs to have a value for field "id" before this many-to-many relationship can be used.
                new_appointment.participants.set(form.cleaned_data["participants"])
                new_appointment.tests.set(form.cleaned_data["tests"])
                # print("try executed")
                return HttpResponseRedirect(reverse("labsys:appointments"))
            except Exception as error:
                # print("excetp executed")
                return render(request, 'labsys/add_Appointment.html', {"pat_id":pat_id, "form": form, "message":error})
        # if form is not valid
        else:
            return render(request, 'labsys/add_Appointment.html', {"pat_id":pat_id,"form": form, "message":form.errors })   
    # if request method get
    return render(request, 'labsys/add_Appointment.html', {"pat_id":pat_id, "form": AppointmentRegistration })

@login_required(login_url='/lab/login/')
def appointments(request):
    if request.method == 'POST':
        date = request.POST["date"]
        appointment_date = Appointment.objects.filter(start__date=date)
        return render(request, 'labsys/appointment.html', {"appointments" :appointment_date, "date" : date})
    #if requestmethod is get load today's appointment by default
    appointment_today = Appointment.objects.filter(start__date=datetime.today().date())
    return render(request, 'labsys/appointment.html', {'appointments':appointment_today})



@login_required(login_url='/lab/login/')
def encounter(request, enc_id):
    e = Encounter.objects.get(pk=enc_id)
    chargeItems = ChargeItem.objects.filter(context= e)
    invoice = Invoice.objects.get(pk=e.invoice.id)
    # filtering payment objects for particular invoice
    payments = PaymentReconciliation.objects.filter(request=invoice)
    #creat set of chargeitemdefinations id included in this encounter(allready added tests)
    test_id_set = []
    # list of all chargeitem defination for the encounter
    ChargeItemsDefinition = e.test.all()
    #add chargeitem id to newly created set
    for t in ChargeItemsDefinition:
        test_id_set.append(t.id)
    #creating observationdefination object queryset excluding those in set ie already register  for the encounter
    # tests = ChargeItemDefinition.objects.exclude(id__in=test_id_set)
    tests =ChargeItemDefinition.objects.filter(prices__pricelist = e.account.pricelist , status = "A").exclude(id__in=test_id_set)
    
    #to check all charge item  is final, first set varialbe to True
    is_all_chargeitem_atleast_final= True
    obs = Observation.objects.filter(chargeitem__in=chargeItems)
    for ob in obs:
        if ob.status == "P" or ob.status == "R":
            is_all_chargeitem_atleast_final = False

    return render(request, 'labsys/encounter.html', {"e" : e, "chargeItems": chargeItems,"payments":payments, "invoice": invoice, "tests":tests, "is_all_chargeitem_atleast_final": is_all_chargeitem_atleast_final} )


@login_required(login_url='/lab/login/')
def chargeitem(request, chargeitem_id, option):
    chargeitem = ChargeItem.objects.get(pk=chargeitem_id)
    # reverse query by related name "observation" 
    observations = chargeitem.observation.all()
    # print(observations)
    # observations = Observation.objects.filter(chargeitem=chargeitem)
    is_all_ob_entered = True
    is_all_ob_final_or_above = True
    for ob in observations:
        #checking if ob.value is not than set variable to false, even single observation is not set it will turn to False
        if not ob.value:
            is_all_ob_entered = False
        #checking if ob.status is either P or R set variable to false, even single observation is not set it will turn to False
        if ob.status == "P" or ob.status == "R":
            is_all_ob_final_or_above = False
    # render different HTML template depending on option: edit, view or preview
    return render(request, f'labsys/obs_by_chgItm_{option}.html', {"observations": observations, "chargeitem" : chargeitem, "is_all_ob_entered":is_all_ob_entered, "is_all_ob_final_or_above": is_all_ob_final_or_above} )


@login_required(login_url='/lab/login/')
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
            telecoms = Telecom.objects.filter(use="M").filter(value=mobno)
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
    
