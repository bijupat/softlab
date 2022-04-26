
from .models import *
from django.db.models import Sum
from django.shortcuts import render, HttpResponse, get_object_or_404


"""
register_encounter takes input
1. Patient Object
2. ChargeItem Definations set
3. Discount
4. Payment amount

and registers new encounter and returns true if all ok
"""
def register_encounter(Patient, Practitioner, Tests, Discount, Payment, Account, User):
    #create new invoice and save without payment details
    inv = Invoice(subject=Patient, participant = Practitioner, account = Account )
    
    #create new encounter instance
    enc = Encounter()
    # assing it's patient attribute to new_patient instance of Patient Class and save
    enc.patient = Patient
    enc.practitioner = Practitioner
    enc.account = Account
    enc.save()
    # populate enc instance with queryset test/form.cleaned_data['test'] (as it it diretely populated from object in form) will return queryset as it is foreingkey(many to one)
    # enc.test is chargeitems for the encounter 
    chageitemdefinations = Tests
    enc.test.set(chageitemdefinations)            
    
    p = enc.test.all().aggregate(Sum('value'))
    paid = Payment
    #populate payment data in invoice object
    inv.discount = Discount
    inv.totalGross = p['value__sum']
    if not inv.totalGross:
        inv.totalGross = 0
    if not inv.discount:
        inv.discount = 0
    if not paid:
        paid = 0
    inv.totalnet = inv.totalGross - inv.discount
    inv.due = inv.totalnet-paid
    if inv.totalnet < 0 or inv.due < 0:
        enc.delete()
        return False

    # save invoice and encounter only after all validation done
    inv.save()
    enc.invoice = inv
    enc.save()

    # filtering charge items for encounter and getting its subject and enterer filed with patient and user
    chargeItems = ChargeItem.objects.filter(context=enc)
    for c in chargeItems:
        c.subject = Patient
        c.enterer = User
        c.account = Account
        #finding set of observationdefs under test(chargeitemdef) by ChargeItemDefinition.objects.get(chargeitem=c)
        # finding set of observations in test(chargeitemdef) by .observations.all()
        observations = ChargeItemDefinition.objects.get(chargeitem=c).observations.all()
        # adding filtered observationdef to chageitem.observation(new_test.observation) as set
        c.observations.set(observations)
        # adding observations from included charge items
        included_tests = c.definitionCanonical.includes.all()
        for t in included_tests:
            for o in t.observations.all():
                c.observations.add(o)
        # to add price overide in chargeitem
        c.priceOverride = c.definitionCanonical.value
        c.save()
            # add default values to observatioin from ob_def    
    observations = Observation.objects.filter(chargeitem__in = chargeItems)
    for o in observations:
        ob_def = o.testfield
        qualifiedIntervals = ob_def.qualifiedinterval
        high, low = "", ""
        for q in qualifiedIntervals.all():
            if q.category == "R":
                high = q.high
                low = q.low
        o.status = "R"
        o.unit = ob_def.unit
        o.high = high
        o.low = low  
        o.note = ob_def.note
        o.save()
    #pat_address = Address()
    #pat_address.use = "home"
    #pat_address.text = form.cleaned_data["Address"]
    #pat_address.save()
    if paid:
        payment = PaymentReconciliation(request=inv, paymentAmount= paid, received_by = User)
        payment.save()
    

    return True