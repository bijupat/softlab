
from .models import Observation, Invoice, Encounter, ChargeItem, ChargeItemDefinition, PaymentReconciliation, Appointment
from django.db.models import Sum


"""
register_encounter takes input
1. Patient Object
2. Practitioner Object
3. ChargeItem Definations set
4. Discount amount (int)
5. Payment amount (int)
6. User Object

and registers new encounter and returns true if all ok
"""
def register_encounter(Patient, Practitioner, Tests, Discount, Payment, Account, User):

    #create new invoice and save without payment details
    inv = Invoice(subject=Patient, participant = Practitioner, account = Account, discount = Discount or 0 )    
    #create new encounter instance
    enc = Encounter(patient = Patient, practitioner = Practitioner, account = Account)
    enc.save()
    # populate enc instance with queryset test/form.cleaned_data['test'] (as it it diretely populated from object in form) will return queryset as it is foreingkey(many to one)
    # enc.test is (through chargeitems) chargeitemdefination for the encounter 
    enc.test.set(Tests)

    # filtering charge items for encounter by reverse quering using related name "chargeitem" and getting its subject and enterer filed with patient and user
    chargeItems = enc.chargeitem.all()
    # chargeItems = ChargeItem.objects.filter(context=enc)
    for c in chargeItems:
        c.subject, c.enterer, c.account = Patient, User, Account
        #finding set of observationdefs under test(chargeitemdef) by ChargeItemDefinition.objects.get(chargeitem=c)
        # finding set of observations in test(chargeitemdef) by .observations.all()
        observations = c.definitionCanonical.observations.all()
        # observations = ChargeItemDefinition.objects.get(chargeitem=c).observations.all()
        # adding filtered observationdef to chageitem.observation(new_test.observation) as set
        c.observations.set(observations)
        # adding observations from included charge items
        included_tests = c.definitionCanonical.includes.all()
        for t in included_tests:
            for o in t.observations.all():
                c.observations.add(o)
        # to add price overide in chargeitem using model method update_price
        c.update_price()
        
        c.save()
    #populate payment data in invoice object
    total = chargeItems.aggregate(Sum('priceOverride'))['priceOverride__sum'] or 0
    totalnet = total - (Discount or 0)
    due = totalnet - (Payment or 0)
    # if payment logically not correct return with false value
    if totalnet < 0 or due < 0 :
        enc.delete()
        return False
    # save invoice in encounter only after all validation done
    inv.save()
    enc.invoice = inv
    enc.save()
    
    # add default values to observatioin from ob_def    
    observations = Observation.objects.filter(chargeitem__in = chargeItems)
    for o in observations:
        # using object instance method
        o.populate_fm_obdef()

    if Payment:
        payment = PaymentReconciliation(request=inv, paymentAmount= Payment, received_by = User)
        payment.save()    

    return True

