from django.db import models
#from django.db.models.base import Model
#from django.db.models.enums import Choices
from django.contrib.auth.models import AbstractUser
from datetime import date
#from django.db.models.fields.related import OneToOneField



# phone | fax | email | pager | url | sms | other
Telecom_system =(
    ("P", "phone"),
    ("F", "fax"),
    ("E", "email"),
    ("U", "url"),
    ("B", "pager"),
    ("S", "sms"),
    ("O", "other"),
)
# // home | work | temp | old | mobile - purpose of this contact point
Telecom_use =(
    ("H", "home"),
    ("W", "work"),
    ("T", "temp"),
    ("O", "old"),
    ("M", "mobile"),
)
 # // usual | official | temp | nickname | anonymous | old | maiden
Name_use =(
    ("U", "usual"),
    ("O", "official"),
    ("T", "temp"),
    ("N", "nickname"),
    ("A", "anonymous"),
    ("D", "old"),
    ("M", "maiden"),
 )
 # // home | work | temp | old | billing - purpose of this address
Address_use =(
    ("H", "home"),
    ("W", "work"),
    ("T", "temp"),
    ("O", "old"),
    ("B", "billing"),
 )

Contact_relationship =(
    ("H", "Husband"),
    ("W", "Wife"),
    ("F", "Father"),
    ("M", "Mother"),
    ("B", "Brother"),
    ("S", "Sister"),
    ("Fr", "Friend"),
    ("FI", "Father in law"),
    ("MI", "Mother in law"),
    ("BI", "Brother in law"),
    ("SI", "Sister in law"),
    ("O", "Other(specify with name)")
 )


"""
Male.	Male
Female.	Female
Other.	The administrative gender is a value other than male/female/unknown. Where this value is selected, systems may often choose to include an extension with the localized more specific value.
Unknown. A proper value is applicable (field value is there), but not known. Usage Notes: This means the actual value is not known(but is there like home tele is there but no is not known) etc.), then the OTH or UNC flavor should be used. No properties should be included for a datatype with this property unless: Those properties themselves directly translate to a semantic of "unknown". (E.g. a local code sent as a translation that conveys 'unknown') Those properties further qualify the nature of what is unknown. (E.g. 
"""
gender =(
    ("M", "Male"),
    ("F", "Female"),
    ("U", "Unknown"),
    ("O", "Other"),
)

"""
A	Annulled :	Marriage contract has been declared null and to not have existed
D	Divorced :	Marriage contract has been declared dissolved and inactive
I	Interlocutory :	Subject to an Interlocutory Decree.
L	Legally Separated	
M	Married:A current marriage contract is active
P	Polygamous :	More than 1 current spouse
S	Never Married :	No marriage contract has ever been entered
T	Domestic partner :	Person declares that a domestic partner relationship exists.
U	unmarried :	Currently not in a marriage contract.
W	Widowed	: The spouse has died
"""
marital_status =(
    ("A", "Annulled"),
    ("D", "Divorced"),
    ("I", "Interlocutory"),
    ("L", "Legally Separated"),
    ("M", "Married"),
    ("P", "Polygamous"),
    ("S", "Never Married"),
    ("T", "Domestic partner"),
    ("u", "Unmarried"),
    ("W", "Widowed"),
 )
#A language which may be used to communicate with the patient about his or her health.
communication = (
    ("G", "Gujarati"),
    ("Hi", "Hindi"),
    ("Pa", "Punjabi"),
    ("Kn", "Kannada"),
    ("Ml", "Malayalam"),
    ("Ne", "Nepali"),
    ("Or", "Odia"),
    ("Mr", "Marathi"),
    ("Bn", "Bengali"),
    ("T", "Tamil"),
    ("Ur", "Urdu"),
    ("E", "English"),
)
# active | inactive | entered-in-error | on-hold | unknown
Account_status = (
    ("A", "Active"),
    ("I", "Inactive"),
    ("E", "entered-in-error"),
    ("H", "on-hold"),
    ("U", "unknown"),
)
Account_type = (
    ("P", "Periodic"),
    ("C", "Cash"),
    ("T", "Temporary"),
)
# social-history/vital-signs/imaging/laboratory/procedure/survey/exam/therapy/activity
ObservationDefinition_category =(
    ("SH", "social-history"),
    ("I", "imaging"),
    ("L", "laboratory"),
    ("P", "procedure"),
    ("S", "survey"),
    ("E", "exam"),
    ("T", "therapy"),
    ("A", "activity"),
)
# registered | preliminary | final | amended
Observation_status= (
    ("R", "registered"),
    ("P", "preliminary"),
    ("F", "final"),
    ("A", "amended"),
)
"""
ObservtionDefination.qualifiedinterval.category
reference	reference range	Reference (Normal) Range for Ordinal and Continuous Observations.
critical	critical range	Critical Range for Ordinal and Continuous Observations.
absolute	absolute range	Absolute Range for Ordinal and Continuous Observations. Results outside this range are not possible.
"""
qualifiedInterval_category= (
    ("R", "reference"),
    ("C", "critical"),
    ("A", "absolute"),
)
class User(AbstractUser) :
    pass

class Period(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()
    """
    patient = models.ForeignKey(Patient, on_delete=models.PROTECT, related_name='patient_period', blank=True, null=True)
    practitioner = models.ForeignKey(Practitioner, on_delete=models.PROTECT, related_name='practitioner_period', blank=True, null=True)
    #contact = models.ForeignKey(Contact, on_delete=models.PROTECT, related_name='Contact_Telecom',blank=True, null=True)
    #name = models.ForeignKey(Name, on_delete=models.PROTECT, related_name='Contact_Telecom',blank=True, null=True)
    """
    def __str__(self):
            return 'Period for Starts :{}/{}/{} and Ends :{}/{}/{} (dd/mm/yyyy)'.format(self.start.day, self.start.month, self.start.year, self.end.day, self.end.month, self.end.year)
 


class Practitioner(models.Model):
    identifier = models.CharField(max_length=75, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True, default=True)
    #name = models.OneToOneField(name, on_delete=models.PROTECT, related_name='practitioner_name')
    #telecom = models.ManyToManyField(telecom, related_name='practitioner_telecom')
    gender = models.CharField(max_length=20, choices=gender,blank=True, null=True)
    birthDate = models.DateField(blank=True, null=True)
    deceasedBoolean = models.BooleanField(blank=True, null=True, default=False)
    #address =  models.ManyToManyField(address, related_name='p                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         fractitioner_Address')
    photo = models.ImageField(blank=True, null=True)
    qualification = models.CharField(max_length=200, blank=True, null=True)
     #A language which may be used to communicate with the patient about his or her health.
    communication = models.CharField(max_length=25, choices=communication, blank=True, null=True)
    period = models.ForeignKey(Period, on_delete=models.PROTECT, related_name='practitioner_period',blank=True, null=True)

    def __str__(self):
        #return self.practitioner_name.all()
        if self.practitioner_name:
            return 'Ref By : Dr {} {}'.format(self.practitioner_name.get().text, self.practitioner_name.get().family)
        else :
            return f'Practitioner id {self.id}'

# // A contact party (e.g. guardian, partner, friend) for the patient##
class Contact(models.Model):
    # // The kind of relationship
    relationship = models.CharField(max_length=75, blank=True, null=True, choices= Contact_relationship)
    # A name associated with the contact person
    gender = models.CharField(max_length=20, blank=True, null=True, choices=gender)
    #period = models.OneToOneField(period, on_delete=models.PROTECT, blank=True, null=True)
    def __str__(self):
        if self.contact_name.get():
            return 'Contact id-{}: Relationship {} between {}(Contact) and {}(Patient)'.format(self.id, self.get_relationship_display(), self.contact_name.get().text, self.patient_contact.get().patient_name.get().text)
        else:
            return 'some error'

class Note(models.Model):
    author = models.ForeignKey(Practitioner, on_delete=models.PROTECT, related_name='author_note')
    time = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=500, blank=True, null=True)    
    def __str__(self):
            return 'Note by : {} at : {}'.format(self.author.practitioner_name.get().text, self.time)

class Patient(models.Model):
    identifier = models.CharField(max_length=75, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True, default=True)
    #name = models.ForeignKey(name, on_delete=models.PROTECT, related_name='Patient_Name')
    birthDate = models.DateField(blank=True, null=True)
    deceasedBoolean = models.BooleanField(blank=True, null=True, default=False)
    gender = models.CharField(max_length= 10, choices=gender,blank=True, null=True)
    #address = models.ForeignKey(address, on_delete=models.PROTECT, related_name='Patient_Address')
    photo = models.ImageField(blank=True, null=True)
    marital_status = models.CharField(max_length=25, choices = marital_status,blank=True, null=True)
    concact = models.ForeignKey(Contact, on_delete=models.PROTECT, related_name='patient_contact',blank=True, null=True)     
    #practitioner = models.ForeignKey(Practitioner, on_delete=models.PROTECT, related_name='Ref_by_GP',blank=True, null=True)
    #A language which may be used to communicate with the patient about his or her health.
    communication = models.CharField(max_length=25, choices=communication, blank=True, null=True)
    period = models.ForeignKey(Period, on_delete=models.PROTECT, related_name='patient_period',blank=True, null=True)
    DisplayFields = ['id', 'active', 'gender', 'age ']

    class Meta:
        ordering = ["id"]
    
    @property
    def age(self):
        if self.birthDate:
            age = date.today().year - self.birthDate.year
            return age

    def __str__(self):
        if self.patient_name:
            return '{} {} (ID : {}) : {} Yrs/{}'.format(self.patient_name.get().text, self.patient_name.get().family, self.id, self.age, self.gender )
        else :
            return f'Patient id : {self.id}'

 

class Telecom(models.Model):
    # phone | fax | email | pager | url | sms | other
    system = models.CharField(max_length=75, choices= Telecom_system)
    # The actual contact point details
    value = models.CharField(max_length=75,)
    # // home | work | temp | old | mobile - purpose of this contact point
    use = models.CharField(max_length=75, choices=Telecom_use)
    # // Specify preferred order of use (1 = highest)
    rank = models.IntegerField(blank=True, null=True)
    patient = models.ForeignKey(Patient, on_delete=models.PROTECT, related_name='patient_telecom', blank=True, null=True)
    practitioner = models.ForeignKey(Practitioner, on_delete=models.PROTECT, related_name='practitioner_telecom', blank=True, null=True)
    contact = models.ForeignKey(Contact, on_delete=models.PROTECT, related_name='contact_telecom',blank=True, null=True)

    def __str__(self):
        if self.patient:
            return 'patient {} {} has {} ({}) : {}'.format(self.patient.patient_name.get().text, self.patient.patient_name.get().family ,self.get_system_display(), self.get_use_display(), self.value)
        if self.practitioner:
            return 'Practitioner {} {} has {} ({}) : {}'.format(self.practitioner.practitioner_name.get().text, self.practitioner.practitioner_name.get().family ,self.get_system_display(), self.get_use_display(), self.value)
        if self.contact:
            return 'Practitioner {} {} has {} ({}) : {}'.format(self.contact.contact_name.get().text, self.contact.contact_name.get().family ,self.get_system_display(), self.get_use_display(), self.value)

class Name(models.Model):
    # // usual | official | temp | nickname | anonymous | old | maiden
    use = models.CharField(max_length=7, blank=True, null=True, choices =Name_use)
    # // Text representation of the full name   
    text = models.CharField(max_length=75)
    # // Family name (often called 'Surname')
    family = models.CharField(max_length=75, blank=True, null=True)
    # // Given names (not always 'first'). Includes middle names
    given = models.CharField(max_length=75, blank=True, null=True)
    # // Parts that come before the name
    prefix = models.CharField(max_length=75, blank=True, null=True)
    # // Parts that come after the name
    suffix = models.CharField(max_length=75, blank=True, null=True)
    # Time period when name was/is in use
    patient = models.ForeignKey(Patient, on_delete=models.PROTECT, related_name='patient_name', blank=True, null=True)
    practitioner = models.ForeignKey(Practitioner, on_delete=models.PROTECT, related_name='practitioner_name', blank=True, null=True)
    contact = models.ForeignKey(Contact, on_delete=models.PROTECT, related_name='contact_name',blank=True, null=True)
    #period = models.OneToOneField(period, on_delete=models.PROTECT, blank=True)

    def __str__(self):
        if self.patient:
            return 'Patient : {} {} having  id {}'.format(self.text, self.family, self.patient.id)
        if self.practitioner:
            return 'Practitioner : {} {} having  id {}'.format(self.text, self.family, self.practitioner.id)
        if self.contact:
            return 'Contact : {} {} having  id {}'.format(self.text, self.family, self.contact.id)

class Address(models.Model):
    # // home | work | temp | old | billing - purpose of this address
    use = models.CharField(max_length=75, choices=Address_use)
    # // Text representation of the address
    text = models.CharField(max_length=250)
    # // Street name, number, direction & P.O. Box etc.
    line = models.CharField(max_length=250)
    # // Name of city, town etc.
    city = models.CharField(max_length=75)
    district = models.CharField(max_length=75, default="Ahmedabad")
    state = models.CharField(max_length=250, default="Gujarat")
    postalCode = models.CharField(max_length=250)
    country = models.CharField(max_length=250, default="India")
    patient = models.ForeignKey(Patient, on_delete=models.PROTECT, related_name='patient_address', blank=True, null=True)
    practitioner = models.ForeignKey(Practitioner, on_delete=models.PROTECT, related_name='practitioner_address', blank=True, null=True)
    contact = models.ForeignKey(Contact, on_delete=models.PROTECT, related_name='contact_address',blank=True, null=True)
    # Time period when name was/is in use
    #period = models.OneToOneField(period, on_delete=models.PROTECT, blank=True, null=True)
    def __str__(self):
        if self.patient:
            return 'address for : {} {}(Patient) at({}) : {}'.format(self.patient.patient_name.get().text, self.patient.patient_name.get().family, self.get_use_display(), self.text)
        if self.practitioner:
            return 'address for : {} {}(Practitioner) at({}) : {}'.format(self.practitioner.practitioner_name.get().text, self.practitioner.practitioner_name.get().family, self.get_use_display(), self.text)
        if self.contact:
            return 'address for : {} {} (Contact) at({}) : {}'.format(self.contact.contact_name.get().text, self.contact.contact_name.get().family, self.get_use_display(), self.text)
        else:
            return 'Some error'


class Account (models.Model):
    identifier = models.CharField(max_length=75, blank=True, null=True)
    # active | inactive | entered-in-error | on-hold | unknown
    status = models.CharField(max_length=75, blank=True, null=True, choices= Account_status)
    #patient = models.ForeignKey(Patient, on_delete=models.PROTECT, related_name='patient_account', blank=True, null=True)
    # patient, expense, depreciation
    type = models.CharField(max_length=75, blank=True, null=True, choices=Account_type)
    #// Human-readable label
    name = models.CharField(max_length=75, blank=True, null=True)
    #Explanation of purpose/use
    description = models.CharField(max_length=75, blank=True, null=True)    

    def __str__(self):
            return 'Account  : {}'.format(self.name)


#master data class
class Pricelist(models.Model):
    pricelist = models.CharField(max_length=75, blank=True, null=True)
    account = models.ForeignKey(Account, on_delete=models.PROTECT, related_name='pricelist_account')
    
    def __str__(self):
            return 'Pricelist : {}'.format(self.pricelist)

class Sampletype(models.Model):
    sampletype = models.CharField(max_length=75, blank=True, null=True)
    #test = models.ManyToManyField(ObservationDefination, related_name='sampletype_test')

    def __str__(self):
            return 'SampleType : {}'.format(self.sampletype)

class TestCategory(models.Model):
    category = models.CharField(max_length=75, blank=True, null=True)

    def __str__(self):
            return 'Category : {}'.format(self.category)

class Organization (models.Model):
    pass


#master list of observations(Testlist)
class ObservationDefinition(models.Model):
    # use loinic Consumer Name if possible
    test = models.CharField(max_length=75, blank=True, null=True)
    # general name usded in routine practice
    alias = models.CharField(max_length=75, blank=True, null=True)
    price = models.PositiveIntegerField(blank=True, null=True)
    #sample_type = models.ManyToManyField(Sampletype,on_delete=models.PROTECT, related_name='test_sampletype', blank=True, null=True)
    pricelist_included = models.ManyToManyField(Pricelist, related_name='observationdefination_pricelist', blank=True)
    sampletype = models.ForeignKey(Sampletype, on_delete=models.PROTECT, related_name='observationdefination_sampletype', blank=True, null=True)
    method = models.CharField(max_length=75, blank=True, null=True)
    category = models.ForeignKey(TestCategory, on_delete=models.PROTECT, related_name='observationdefination_testcategory', blank=True, null=True)
    outsourced_to = models.ForeignKey(Organization, on_delete=models.PROTECT, related_name='observationdefination_organization', blank=True, null=True)
    unit = models.CharField(max_length=75, blank=True, null=True)
    loinc_code = models.CharField(max_length=75, blank=True, null=True)
    #The low and high values determining the interval. There may be only one of the two
    qualifiedInterval_range = models.JSONField(blank=True, null=True)
    # social-history/vital-signs/imaging/laboratory/procedure/survey/exam/therapy/activity
    category = models.CharField(max_length=75, blank=True, null=True, choices=ObservationDefinition_category, default="laboratory")

    class Meta:
        ordering = ["test"]

    def __str__(self):
            return 'Test : {}  price : {}'.format(self.test, self.price)

# Referance range for testlist(observationdefination)
class QualifiedInterval(models.Model):
    high = models.CharField(max_length=75, blank=True, null=True)
    low = models.CharField(max_length=75, blank=True, null=True)
    # category can be reference | critical | absolute
    category = models.CharField(max_length=10, choices=qualifiedInterval_category)
    age_high = models.PositiveIntegerField(blank=True)
    age_low = models.PositiveIntegerField(blank=True)
    gender = models.CharField(max_length=20, choices=gender,blank=True, null=True)
    observationdefinition = models.ForeignKey(ObservationDefinition, on_delete=models.PROTECT, related_name='qualifiedinterval_observationdefination', blank=True, null=True)
    gestationalAge = models.CharField(max_length=50, blank=True, null=True)
    #Text based condition for which the reference range is valid.
    condition = models.CharField(max_length=75, blank=True, null=True)
   

    def __str__(self):
            return 'pending'

class Invoice(models.Model):
    identifier = models.CharField(max_length=75, blank=True, null=True)
    # draft | issued | balanced | cancelled | entered-in-error
    status = models.CharField(max_length=75, blank=True, null=True, default='registered')
    cancelled_reason = models.CharField(max_length=200, blank=True, null=True)
    # Recipient(s) of goods and services
    subject = models.ForeignKey(Patient, on_delete=models.PROTECT, related_name='invoice_subject', blank=True, null=True)
    # Recipient of this invoice
    recipient = models.ForeignKey(Organization, on_delete=models.PROTECT, related_name='invoice_recipient', blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    # Participant in creation of this Invoice
    participant = models.ForeignKey(Practitioner, on_delete=models.PROTECT, related_name='invoice_participant', blank=True, null=True)
    account = models.ForeignKey(Account, on_delete=models.PROTECT, related_name='invoice_participant', blank=True, null=True)
    #lineItem = models.ForeignKey(ObservationDefinition, on_delete=models.PROTECT, related_name='invoice_observationdefination', blank=True, null=True)
    # Invoice total, discount excluded.
    totalGross = models.PositiveIntegerField(blank=True, null=True)
    discount = models.PositiveIntegerField(blank=True, null=True)
    # Invoice total after discount.
    totalnet = models.PositiveIntegerField(blank=True, null=True)   
    # Payment details such as banking details, period of payment, deductibles, methods of payment.
    due = models.PositiveIntegerField(blank=True, null=True)
    paymentTerms = models.CharField(max_length=200, blank=True, null=True)
    # Comments made about the invoice by the issuer, subject, or other participants.
    note = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f' Inovoice id {self.id} for {self.subject}'


class Encounter(models.Model):
    identifier = models.CharField(max_length=75, blank=True, null=True)
    test = models.ManyToManyField(ObservationDefinition, through='Observation', related_name='Encounter_observationdefination')
    #observation = models.ForeignKey(Observation, on_delete=models.PROTECT, related_name='encounter_observation', blank=True, null=True)
    #test = models.ForeignKey(ObservationDefination, on_delete=models.PROTECT, related_name='encounter_observationdefination', blank=True, null=True)
    # planned | arrived | triaged | in-progress | onleave | finished | cancelled
    status = models.CharField(max_length=75, blank=True, null=True)
    patient = models.ForeignKey(Patient, on_delete=models.PROTECT, related_name='patient_encounter', blank=True, null=True)
    practitioner = models.ForeignKey(Practitioner, on_delete=models.PROTECT, related_name='practitioner_encounter', blank=True, null=True)
    account = models.ForeignKey(Account, on_delete=models.PROTECT, related_name='account_encounter', blank=True, null=True)
    # one invoice can be created for more than one encounter
    invoice = models.ForeignKey(Invoice, on_delete=models.PROTECT, related_name='invoice_encounter', blank=True, null=True)
    timedate = models.DateTimeField(auto_now_add=True)
    #contact = models.ForeignKey(Contact, on_delete=models.PROTECT, related_name='Contact_Telecom',blank=True, null=True)
    #name = models.ForeignKey(Name, on_delete=models.PROTECT, related_name='Contact_Telecom',blank=True, null=True)
    
    class Meta:
        ordering = ["timedate"]
    
    def __str__(self):
            return 'Encounter id {} for Patient : {} at {}'.format(self.id, self.patient.patient_name.get().text, self.timedate)

class Observation(models.Model):
    identifier = models.CharField(max_length=75, blank=True, null=True)
    # registered | preliminary | final | amended +
    status = models.CharField(max_length=75, blank=True, null=True, default='registered',  choices= Observation_status)
    entered_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='observation_entered_by', blank=True, null=True)
    verified_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='observation_verfied_by', blank=True, null=True)
    #account = models.ForeignKey(Account, on_delete=models.PROTECT, related_name='observation_account', blank=True, null=True)
    timedate = models.DateTimeField(auto_now_add=True)
    test = models.ForeignKey(ObservationDefinition, related_name='observation_observationdefination', on_delete=models.PROTECT, blank=True, null=True)
    value = models.CharField(max_length=200, blank=True, null=True)
    interpretation = models.CharField(max_length=200, blank=True, null=True)
    encounter = models.ForeignKey(Encounter, on_delete=models.PROTECT, related_name='observation_encounter', blank=True, null=True)
    # add Ref high and low value based on patient age and sex from observationdefination qualified interval
    # this will not change even if we change it in observationdefination qualifed interval so it will not take retrospective effect
    high = models.CharField(max_length=75, blank=True, null=True)
    low = models.CharField(max_length=75, blank=True, null=True)
    # add price from observationdefination based on price, we can edit it later, also price changed in observationdefination will not take retrospective effect
    price = models.PositiveIntegerField(blank=True, null=True)

    class Meta:
        ordering = ["-timedate"]
    
    def __str__(self):
        if self.encounter and self.test:
            return 'Observation : {} for Patient : {} for test {} on Encounter id : {}'.format(self.id, self.encounter.patient.patient_name.get().text, self.test.test, self.encounter.id)
        else:
            return 'You need to enter observation using Encounter model'
    
class DiagnosticReport (models.Model):
    pass


class PaymentReconciliation(models.Model):
    identifier = models.CharField(max_length=75, blank=True, null=True)
    #  active | cancelled | draft | entered-in-error
    status = models.CharField(max_length=75, blank=True, null=True, default='registered')
    # Creation date The date when the resource was created.
    created = models.DateTimeField(auto_now_add=True)
    # Need to identify the party resonsible for the payment and this resource.
    payment_issuer = models.ForeignKey(Organization, on_delete=models.PROTECT, related_name='paymentreconciliation_issuer', blank=True, null=True)
    # Reference to requesting resource (Invoice)
    request = models.ForeignKey(Invoice, on_delete=models.PROTECT, related_name='paymentreconciliation_issuer', blank=True, null=True)
    #payment received by user
    received_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='payment_received_by', blank=True, null=True)
    # When payment issued
    paymentDate = models.DateField(auto_now_add=True)
    # Total amount of Payment Total payment amount as indicated on the financial instrument.
    paymentAmount = models.PositiveIntegerField(blank=True, null=True)
    # The period of time for which payments have been gathered into this bulk payment for settlement.(For Periodic Accounts )
    period = models.ForeignKey(Period, on_delete=models.PROTECT, related_name='paymentreconciliation_period',blank=True, null=True)

    """    Payment types
    Code		Definition
    payment		The amount is partial or complete settlement of the amounts due.
    adjustment	The amount is an adjustment regarding claims already paid.
    advance		The amount is an advance against future claims.
    """
    type = models.CharField(max_length=10, blank=True, null=True)
    note = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f' Payment id {self.id}'

