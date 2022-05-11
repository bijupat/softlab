#from xml.etree.ElementInclude import include
from django.db import models
#from django.db.models.base import Model
#from django.db.models.enums import Choices
from django.contrib.auth.models import AbstractUser
from datetime import date
#from django.db.models.fields.related import OneToOneField
#from django.contrib.postgres.fields import JSONField



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
    ("R", "Registered"),
    ("P", "Preliminary"),
    ("F", "Final"),
    ("I", "Informed"),
    ("D", "Delivered"),
    ("A", "Amended"),
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
    #name = models.OneToOneField(name, on_delete=models.PROTECT, related_name='name')
    #telecom = models.ManyToManyField(telecom, related_name='practitioner_telecom')
    gender = models.CharField(max_length=20, choices=gender,blank=True, null=True)
    birthDate = models.DateField(blank=True, null=True)
    deceasedBoolean = models.BooleanField(blank=True, null=True, default=False)
    #address =  models.ManyToManyField(address, related_name='p                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         fractitioner_Address')
    photo = models.ImageField(blank=True, null=True)
    qualification = models.CharField(max_length=200, blank=True, null=True)
     #A language which may be used to communicate with the patient about his or her health.
    communication = models.CharField(max_length=25, choices=communication, blank=True, null=True)
    period = models.ForeignKey(Period, on_delete=models.PROTECT, related_name='practitioner',blank=True, null=True)

    def __str__(self):
        #return self.name.all()
        if self.name:
            return 'Dr {} {}'.format(self.name.get().text.title(), self.name.get().family.title())
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
        if self.name.get():
            return 'Contact id-{}: Relationship {} between {}(Contact) and {}(Patient)'.format(self.id, self.get_relationship_display(), self.name.get().text, self.patient.get().name.get().text)
        else:
            return 'some error'



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
    concact = models.ForeignKey(Contact, on_delete=models.PROTECT, related_name='patient',blank=True, null=True)     
    #practitioner = models.ForeignKey(Practitioner, on_delete=models.PROTECT, related_name='Ref_by_GP',blank=True, null=True)
    #A language which may be used to communicate with the patient about his or her health.
    communication = models.CharField(max_length=25, choices=communication, blank=True, null=True)
    period = models.ForeignKey(Period, on_delete=models.PROTECT, related_name='patient',blank=True, null=True)

    class Meta:
        ordering = ["id"]
    # implenting age field to be calculated from birth date
    @property
    def age(self):
        if self.birthDate: 
            return date.today().year - self.birthDate.year

    # defining method that returns usual name
    def get_usual_name(self):
        if self.name:
            for name in self.name.all():
                if name.use == "U":
                 return '{} {}'.format(name.text, name.family)
    # defining method that returns mobile no
    def get_mobile(self):
        if self.name:
            for tele in self.telecom.all():
                if tele.use == "M":
                    return '{}'.format(tele.value)
    # defining method that returns e mail
    def get_email(self):
        if self.name:
            for tele in self.telecom.all():
                if tele.system == "E":
                    return '{}'.format(tele.value)

    def __str__(self):
        if self.name:
            for name in self.name.all():
                if name.use == "U":
                    fname = name.text
                    lname = name.family
            return '{} {} : {} Yrs/{} (ID : {})'.format(fname, lname , self.age, self.gender, self.id)
        else :
            return f'Patient id : {self.id}'

class Organization (models.Model):
    identifier = models.CharField(max_length=75, blank=True, null=True)
    # Whether the organization's record is still in active use
    active = models.BooleanField(blank=True, null=True, default=True)
    #Name used for the organization
    name = models.CharField(max_length=75, blank=True, null=True)
    # A list of alternate names that the organization is known as, or was known as in the past
    alias = models.CharField(max_length=75, blank=True, null=True)
    # Contact for the organization for a certain purpose 
    contact = models.ForeignKey(Contact, on_delete=models.PROTECT, related_name='organization',blank=True, null=True)


    def __str__(self):
            return 'Organizasion  : {}'.format(self.name)




class Telecom(models.Model):
    # phone | fax | email | pager | url | sms | other
    system = models.CharField(max_length=10, choices= Telecom_system)
    # The actual contact point details
    value = models.CharField(max_length=75,)
    # // home | work | temp | old | mobile - purpose of this contact point
    use = models.CharField(max_length=10, choices=Telecom_use)
    # // Specify preferred order of use (1 = highest)
    rank = models.IntegerField(blank=True, null=True)
    patient = models.ForeignKey(Patient, on_delete=models.PROTECT, related_name='telecom', blank=True, null=True)
    practitioner = models.ForeignKey(Practitioner, on_delete=models.PROTECT, related_name='telecom', blank=True, null=True)
    contact = models.ForeignKey(Contact, on_delete=models.PROTECT, related_name='telecom',blank=True, null=True)
    organization = models.ForeignKey(Organization, on_delete=models.PROTECT, related_name='telecom',blank=True, null=True)

    def __str__(self):
        if self.patient:
            return 'patient {} {} has {} ({}) : {}'.format(self.patient.name.get().text, self.patient.name.get().family ,self.get_system_display(), self.get_use_display(), self.value)
        if self.practitioner:
            return 'Practitioner {} {} has {} ({}) : {}'.format(self.practitioner.name.get().text, self.practitioner.name.get().family ,self.get_system_display(), self.get_use_display(), self.value)
        if self.contact:
            return 'Practitioner {} {} has {} ({}) : {}'.format(self.contact.contact_name.get().text, self.contact.contact_name.get().family ,self.get_system_display(), self.get_use_display(), self.value)
        if self.organization:
            return 'Organization {} has {} ({}) : {}'.format(self.organization.name, self.get_system_display(), self.get_use_display(), self.value)

class Name(models.Model):
    # // usual | official | temp | nickname | anonymous | old | maiden
    use = models.CharField(max_length=7, blank=True, null=True, choices =Name_use, default="U")
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
    patient = models.ForeignKey(Patient, on_delete=models.PROTECT, related_name='name', blank=True, null=True)
    practitioner = models.ForeignKey(Practitioner, on_delete=models.PROTECT, related_name='name', blank=True, null=True)
    contact = models.ForeignKey(Contact, on_delete=models.PROTECT, related_name='name',blank=True, null=True)
    #period = models.OneToOneField(period, on_delete=models.PROTECT, blank=True)

    def serialize(self):
        #if name if for patient it will retun filled dic
        if self.patient:
            mobno = ""
            for t in self.patient.telecom.all():
                if t.use == "M":
                    mobno = t.value
            return{
                "fname": self.text,
                "lname": self.family,
                "patient_id": self.patient.id,
                "mobno": mobno,    
            }
        #if name if of contact or practitioner it will retun empty dict
        else:
            return{
                "fname": "",
                "lname": "",
                "patient_id":"",
                "mobno": "",            
            }

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
    patient = models.ForeignKey(Patient, on_delete=models.PROTECT, related_name='address', blank=True, null=True)
    practitioner = models.ForeignKey(Practitioner, on_delete=models.PROTECT, related_name='address', blank=True, null=True)
    contact = models.ForeignKey(Contact, on_delete=models.PROTECT, related_name='address',blank=True, null=True)
    organization = models.ForeignKey(Organization, on_delete=models.PROTECT, related_name='address',blank=True, null=True)

    # Time period when name was/is in use
    #period = models.OneToOneField(period, on_delete=models.PROTECT, blank=True, null=True)
    def __str__(self):
        if self.patient:
            return 'address for : {} {}(Patient) at({}) : {}'.format(self.patient.name.get().text, self.patient.name.get().family, self.get_use_display(), self.text)
        if self.practitioner:
            return 'address for : {} {}(Practitioner) at({}) : {}'.format(self.practitioner.name.get().text, self.practitioner.name.get().family, self.get_use_display(), self.text)
        if self.contact:
            return 'address for : {} Contact) at({}) : {}'.format(self.contact, self.get_use_display(), self.text)
        if self.organization:
            return 'address for : {} (organization) at({}) : {}'.format(self.organization.name, self.get_use_display(), self.text)
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
    # true if particular account is default
    is_default = models.BooleanField(default=False)
    is_periodic = models.BooleanField(default=False)
    # contact
    contact = models.ForeignKey(Contact, on_delete=models.PROTECT, related_name='account',blank=True, null=True)

    def __str__(self):
            return 'Account  : {}'.format(self.name)


#master data class
class Pricelist(models.Model):
    pricelist = models.CharField(max_length=75, blank=True, null=True)
    account = models.ForeignKey(Account, on_delete=models.PROTECT, related_name='pricelist')
    
    def __str__(self):
            return 'Pricelist : {}'.format(self.pricelist)


class Specimen(models.Model):
    sampletype = models.CharField(max_length=75, blank=True, null=True)
    #test = models.ManyToManyField(ObservationDefination, related_name='sampletype_test')

    def __str__(self):
            return 'SampleType : {}'.format(self.sampletype)

class TestCategory(models.Model):
    category = models.CharField(max_length=75, blank=True, null=True)

    def __str__(self):
            return 'Category : {}'.format(self.category)

  

    
# Master list of depatement like biochem, hemat, histo  

class Department(models.Model):
    pass





#master list of observations(Testlist)
class ObservationDefinition(models.Model):
    # use loinic Consumer Name if possible
    test = models.CharField(max_length=75, blank=True, null=True)
    # general name usded in routine practice
    alias = models.CharField(max_length=75, blank=True, null=True)
    # name used in SMS field
    alias_sms = models.CharField(max_length=20, blank=True, null=True)  
    method = models.CharField(max_length=75, blank=True, null=True)
    category = models.ForeignKey(TestCategory, on_delete=models.PROTECT, related_name='observationdefination', blank=True, null=True)
    unit = models.CharField(max_length=75, blank=True, null=True)
    # option fields in observation defination, implemented as set or other method-- all options in one field
    options = models.CharField(max_length=5000, blank=True, null=True)
    loinc_code = models.CharField(max_length=75, blank=True, null=True)
    #The low and high values determining the interval. There may be only one of the two
    # social-history/vital-signs/imaging/laboratory/procedure/survey/exam/therapy/activity
    category = models.CharField(max_length=75, blank=True, null=True, choices=ObservationDefinition_category, default="laboratory")
    # Specimen Required for this chargeitem/test/report
    specimen = models.ForeignKey(Specimen, on_delete=models.PROTECT, related_name='observationdefination', blank=True, null=True)
    # note specific to the observation
    note = models.CharField(max_length=1000, blank=True, null=True)
    # which department in lab as per department define in model ie biochem, histo etc
    dept = models.ForeignKey(Department,  on_delete=models.PROTECT, related_name='observationdefination', blank=True, null=True)
    # TAT for the field
    tat = models.SmallIntegerField(blank=True, null=True)
    is_calculated = models.BooleanField(blank=True, null=True, default=False)
    # formula if calculated test
    formula = models.CharField(max_length=200, blank=True, null=True)
    # Validation Rule 
    vrule = models.CharField(max_length=200, blank=True, null=True)
    # Validation message if not validated
    vmsg = models.CharField(max_length=30, blank=True, null=True)
    # Validation if must ?.
    vrulemust = models.BooleanField(blank=True, null=True,default=True)
    #The low and high values determining the interval. There may be only one of the two
    # it will be implemented from qulified interval class as foreign  key
    class Meta:
        ordering = ["test"]
    def __str__(self):
            return 'Test : {} '.format(self.test)

# Referance range for testlist(observationdefination)
class QualifiedInterval(models.Model):    
    high = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    low = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    text_as_normal =  models.CharField(max_length=500, blank=True, null=True)
    # category can be reference | critical | absolute
    category = models.CharField(max_length=10, choices=qualifiedInterval_category, default="reference")
    # highest age for the qualified interval EXCLUDING it
    age_high = models.PositiveIntegerField(blank=True, default=150)
    # Lowest  age for the qualified interval INCLUDING it 
    age_low = models.PositiveIntegerField(blank=True, default=0)
    gender = models.CharField(max_length=20, choices=gender,blank=True, null=True)
    observationdefinition = models.ForeignKey(ObservationDefinition, on_delete=models.PROTECT, related_name='qualifiedinterval', blank=True, null=True)
    gestationalAge = models.CharField(max_length=50, blank=True, null=True)
    #Text based condition for which the reference range is valid.
    condition = models.CharField(max_length=75, blank=True, null=True)
    def __str__(self):
            return 'For {} as {} age {} to {} / {}'.format(self.observationdefinition, self.category, self.age_low, self.age_high,  self.gender)

class Invoice(models.Model):
    identifier = models.CharField(max_length=75, blank=True, null=True)
    # draft | issued | balanced | cancelled | entered-in-error
    status = models.CharField(max_length=75, blank=True, null=True, default='registered')
    cancelled_reason = models.CharField(max_length=200, blank=True, null=True)
    # Recipient(s) of goods and services
    subject = models.ForeignKey(Patient, on_delete=models.PROTECT, related_name='invoice', blank=True, null=True)
    # Recipient of this invoice
    recipient = models.ForeignKey(Organization, on_delete=models.PROTECT, related_name='invoice', blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    # Participant in creation of this Invoice
    participant = models.ForeignKey(Practitioner, on_delete=models.PROTECT, related_name='invoice', blank=True, null=True)
    account = models.ForeignKey(Account, on_delete=models.PROTECT, related_name='invoice', blank=True, null=True)
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

    def paid(self):
        total = 0
        for e in self.encounter.all():
            chargeItems = ChargeItem.objects.filter(context=e)
            for c in chargeItems:
                total += c.priceOverride or 0
        self.totalGross = total
        paid = 0
        for p in self.paymentreconciliation.all():
            paid += p.paymentAmount or 0
        self.due = total - (paid + self.discount)
        self.totalnet = total-self.discount
        return paid


    def __str__(self):
        return f' Inovoice id {self.id} for {self.subject}'



class Device(models.Model):
    pass

    def __str__(self):
        return f' Test : '

#The ChargeItemDefinition resource provides the properties that apply to the (billing) codes necessary to calculate costs and prices
class ChargeItemDefinition(models.Model):
    identifier = models.CharField(max_length=75, blank=True, null=True)
    # Name for this charge item definition (human friendly)
    title = models.CharField(max_length=75, blank=True, null=True)
    # general name usded in routine practice
    alias = models.CharField(max_length=75, blank=True, null=True)
    # Creation date The date when the resource was created.
    created = models.DateTimeField(auto_now_add=True)
    #A larger definition of which this particular definition is a component or step
    includes = models.ManyToManyField("self", blank=True,  related_name='chargeitemdef_includes')
    #Completed or terminated request(s) whose function is taken by this new request
    replaces = models.ManyToManyField("self", blank=True,  related_name='chargeitemdef_replaces')
    # draft | active | retired | unknown
    status = models.CharField(max_length=75, blank=True, null=True, default='registered')
    # For testing purposes, not real usage
    experimental = models.BooleanField(blank=True, null=True, default=False)
    # is it individula test or profiel ?
    is_profile = models.BooleanField(blank=True, null=True, default=False)
    # observations(test) included in this charge item
    #observations_included = models.ManyToManyField(ObservationDefinition, blank=True,  related_name='chargeitemdef')
    observations = models.ManyToManyField(ObservationDefinition, blank=True, related_name='chargeitemdef')

    # heading to the report print like Hemogram / Liver function test implemented to whole  report
    heading = models.CharField(max_length=75, blank=True, null=True)
    #Date last changed
    date = models.DateTimeField(blank=True, null=True)
    approvalDate = models.DateTimeField(blank=True, null=True)
    lastReviewDate = models.DateTimeField(blank=True, null=True)
    effectivePeriod = models.ForeignKey(Period,blank=True, null=True, related_name='chargeitemdef', on_delete=models.PROTECT)
    #Monetary amount associated with this
    value = models.PositiveIntegerField(blank=True, null=True)
    specimen = models.ManyToManyField(Specimen, related_name='chargeitemdef', blank=True)
    # if test is outsourced 
    outsourced_to = models.ForeignKey(Organization, on_delete=models.PROTECT, related_name='chargeitemdef', blank=True, null=True)
    # use to filter price list in views.py for observations
    pricelist_included = models.ManyToManyField(Pricelist, related_name='chargeitemdef', blank=True)
    # Note for specific  test like double marker applies to whole report
    Note = models.CharField(max_length=75,blank=True, null=True)
    # Product/equipment charged or used
    product = models.ForeignKey(Device, on_delete=models.CASCADE, related_name='chargeitem', null=True, blank=True)
    # ordering of obseration if more than one observatin involved
    orderBy= models.SmallIntegerField(blank=True, null=True)  


    def __str__(self):
        return f'{self.title} Rs  : {self.value}'  


class Encounter(models.Model):
    identifier = models.CharField(max_length=75, blank=True, null=True)
    test = models.ManyToManyField(ChargeItemDefinition, through='ChargeItem', related_name='encounter')
    #observations = models.ManyToManyField(ObservationDefinition, through='Observation', related_name='encounter')
    # planned | arrived | triaged | in-progress | onleave | finished | cancelled
    status = models.CharField(max_length=75, blank=True, null=True)
    patient = models.ForeignKey(Patient, on_delete=models.PROTECT, related_name='encounter', blank=True, null=True)
    practitioner = models.ForeignKey(Practitioner, on_delete=models.PROTECT, related_name='encounter', blank=True, null=True)
    account = models.ForeignKey(Account, on_delete=models.PROTECT, related_name='encounter', blank=True, null=True)
    # one invoice can be created for more than one encounter
    invoice = models.ForeignKey(Invoice, on_delete=models.PROTECT, related_name='encounter', blank=True, null=True)
    timedate = models.DateTimeField(auto_now_add=True)
    #contact = models.ForeignKey(Contact, on_delete=models.PROTECT, related_name='Contact_Telecom',blank=True, null=True)
    #name = models.ForeignKey(Name, on_delete=models.PROTECT, related_name='Contact_Telecom',blank=True, null=True)
    # if urgent  reporting required 
    urgent=  models.BooleanField(default=False)  # Field name made lowercase.


    class Meta:
        ordering = ["timedate"]
    
    def __str__(self):
            return 'Encounter id {} for Patient : {} at {}'.format(self.id, self.patient.get_usual_name(), self.timedate)



class ChargeItem(models.Model):
    identifier = models.CharField(max_length=75, blank=True, null=True)
    # Resource defining the code of this ChargeItem
    definitionCanonical = models.ForeignKey(ChargeItemDefinition, on_delete=models.CASCADE, null=True, blank=True, related_name='chargeitem')
    # planned | billable | not-billable | aborted | billed | entered-in-error | unknown
    status = models.CharField(max_length=75, blank=True, null=True, default='billed')
    #Part of referenced ChargeItem
    partOf = models.ForeignKey("self", on_delete=models.CASCADE, related_name='chargeitem_partof', null=True, blank=True)
    # Individual service was done for/to
    subject = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='chargeitem', null=True, blank=True)
    # Encounter / Episode associated with event
    context = models.ForeignKey(Encounter, on_delete=models.CASCADE, related_name='chargeitem', null=True, blank=True)
    # When the charged service was applied
    occurrenceDateTime = models.DateTimeField(auto_now_add=True)
    # Price overriding first time as default from chargeitemdefination.value
    priceOverride = models.PositiveIntegerField(blank=True, null=True)
    # Reason for overriding if done aftert first entry the list price/factor
    overrideReason = models.CharField(max_length=200, blank=True, null=True, default="Registration")
    #price override by 
    priceoverrideby = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chargeitem_priceoverrideby', null=True, blank=True)
    # Individual who was entering
    enterer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chargeitem_enterer', null=True, blank=True)
    # Which rendered service is being charged?
    #service = models.ForeignKey(DiagnosticReport, on_delete=models.CASCADE, related_name='chargeitem_diagnosticreport', null=True, blank=True)
    # heading to the report print like Hemogram / Liver function test implemented to whole  report : to be copied from chargeitem Defination

    #heading = models.CharField(max_length=75, blank=True, null=True)

    observations = models.ManyToManyField(ObservationDefinition, through='Observation', related_name='chargeitem')

    # Account to place this charge
    account = models.ForeignKey(Account, on_delete=models.PROTECT, related_name='ChargeItem', blank=True, null=True)
    # copies  from charge item defination but open for edit if desired
    note = models.CharField(max_length=1000, blank=True, null=True)

    def is_all_atleat_final(self):
        obs = Observation.objects.filter(chargeitem = self)
        for ob in obs:
            if ob.status == "P" or ob.status == "R":
                return False
        return True

    def __str__(self):
        return f' id : {self.id} Test : {self.definitionCanonical} for Enc : {self.context.id}'

class Observation(models.Model):
    identifier = models.CharField(max_length=75, blank=True, null=True)
    # registered | preliminary | final | amended + |informed | delivered
    status = models.CharField(max_length=75, blank=True, null=True, default='registered',  choices= Observation_status)
    # change staus to preliminary if report entered by operator(entered in pplus)
    prelimnary_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='observation_prelimnary_by', blank=True, null=True)
    # changes to final if reported  is verified by pathologist(verified in pplus)
    final_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='observation_final_by', blank=True, null=True)
    # changes to informed if reported  is informed by user
    informed_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='observation_informed_by', blank=True, null=True)
    # changes to dlivered if delivered
    delivered_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='observation_delivered_by', blank=True, null=True)
    # changes to amended if amended
    amended_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='observation_amended_by', blank=True, null=True)
    #account = models.ForeignKey(Account, on_delete=models.PROTECT, related_name='observation_account', blank=True, null=True)
    
    # Foreign Key to Chargeitem as requirement of through model; this model is intermediate model
    chargeitem = models.ForeignKey(ChargeItem, on_delete=models.PROTECT, related_name='observation', blank=True, null=True)

    # timedate when registed
    timedate = models.DateTimeField(auto_now_add=True)
    # timedate when prelimnary report added
    prelimnary_timedate = models.DateTimeField(blank=True, null=True)
    # timedate when final report added
    final_timedate = models.DateTimeField(blank=True, null=True)
    # timedate when amedded report added
    amended_timedate = models.DateTimeField(blank=True, null=True)
    # timedate when informed report
    informed_timedate = models.DateTimeField(blank=True, null=True)
    # timedate when delivered report 
    delivered_timedate = models.DateTimeField(blank=True, null=True)
    testfield = models.ForeignKey(ObservationDefinition, related_name='observation', on_delete=models.PROTECT, blank=True, null=True)
    # result of the test 
    value = models.CharField(max_length=500, blank=True, null=True)
    # copied from observationdefination.unit but open for change if desired
    unit = models.CharField(max_length=75, blank=True, null=True)
    # to be added to print format if desired
    interpretation = models.CharField(max_length=200, blank=True, null=True)
    #encounter = models.ForeignKey(Encounter, on_delete=models.PROTECT, related_name='observation', blank=True, null=True)
    # add Ref high and low value based on patient age and sex from observationdefination qualified interval
    # this will not change even if we change it in observationdefination qualifed interval so it will not take retrospective effect
    high = models.CharField(max_length=75, blank=True, null=True)
    low = models.CharField(max_length=75, blank=True, null=True)
    # copied from observation defination note  but open to be edited if desired    
    note = models.CharField(max_length=1000, blank=True, null=True)

    def refinterval(self):
        refints = self.testfield.qualifiedinterval.all()
        self.high, self.low = "", ""
        for refint in refints:
            if refint.category == "R":
                if refint.text_as_normal:
                    self.high, self.low = refint.text_as_normal, ""
                elif self.chargeitem.subject.age in range(int(refint.age_low), int(refint.age_high)) and self.chargeitem.subject.gender == refint.gender:
                    self.high, self. low = refint.high, refint.low

    class Meta:
        ordering = ["-timedate"]
    
    def __str__(self):
        if self.chargeitem and self.testfield:
            return 'Observation : {} for Patient : {} for test {} on Encounter id : {}'.format(self.id, self.chargeitem.context.patient.name.get().text, self.testfield.test, self.chargeitem.context.id)
        else:
            return 'You need to enter observation using Encounter model'

class Media(models.Model):
    pass

"""
class DiagnosticReport (models.Model):
    identifier = models.CharField(max_length=75, blank=True, null=True)
    # registered | partial | preliminary | final +
    status = models.CharField(max_length=75, blank=True, null=True, default='registered')
    # https://www.hl7.org/fhir/valueset-diagnostic-service-sections.html
    category = models.CharField(max_length=75, blank=True, null=True)
    #Name/Code for this diagnostic report
    code = models.CharField(max_length=75, blank=True, null=True)
    subject = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='diagnositcreport_patient', null=True, blank=True)
    encounter = models.ForeignKey(Encounter, on_delete=models.CASCADE, related_name='diagnositcreport_encounter', null=True, blank=True)
    effectiveDateTime = models.DateTimeField(blank=True, null=True)
    # person Responsible Diagnostic Service equivalent to ENTERED by in pplus
    performer = models.ForeignKey(User, on_delete=models.PROTECT, related_name='diagnositcreport_performer', blank=True, null=True)
    # person Responsible Diagnostic Service equivalent to verified by in pplus
    resultsInterpreter = models.ForeignKey(User, on_delete=models.PROTECT, related_name='diagnositcreport_resultinterpreter', blank=True, null=True)
    # Specimens this report is based on
    specimen = models.ForeignKey(Specimen, on_delete=models.PROTECT, related_name='diagnositcreport_specimen', blank=True, null=True)
    result = models.ForeignKey(Observation, on_delete=models.PROTECT, related_name='diagnositcreport_observation', blank=True, null=True)
    media_link = models.ForeignKey(Media, on_delete=models.PROTECT, related_name='diagnositcreport_media', blank=True, null=True)
    conclusion = models.CharField(max_length=75, blank=True, null=True, default='registered')
    # Entire report as issued Rich text representation of the entire result as issued by the diagnostic service 
    # can be equivalent to layout in pplus rtf data
    presentedForm = models.CharField(max_length=1000, blank=True, null=True)
    def __str__(self):
        return f' Payment id {self.code}'
"""


class PaymentReconciliation(models.Model):
    identifier = models.CharField(max_length=75, blank=True, null=True)
    #  active | cancelled | draft | entered-in-error
    status = models.CharField(max_length=75, blank=True, null=True, default='active')
    # Creation date The date when the resource was created.
    created = models.DateTimeField(auto_now_add=True)
    # Need to identify the party resonsible for the payment and this resource.
    payment_issuer = models.ForeignKey(Organization, on_delete=models.PROTECT, related_name='paymentreconciliation', blank=True, null=True)
    # Reference to requesting resource (Invoice)
    request = models.ForeignKey(Invoice, on_delete=models.PROTECT, related_name='paymentreconciliation', blank=True, null=True)
    #payment received by user
    received_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='payment_received_by', blank=True, null=True)
    # When payment issued
    paymentDate = models.DateField(auto_now_add=True)
    # Total amount of Payment Total payment amount as indicated on the financial instrument.
    paymentAmount = models.PositiveIntegerField(blank=True, null=True)
    # The period of time for which payments have been gathered into this bulk payment for settlement.(For Periodic Accounts )
    period = models.ForeignKey(Period, on_delete=models.PROTECT, related_name='paymentreconciliation',blank=True, null=True)

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



class Note(models.Model):
    author = models.ForeignKey(Practitioner, on_delete=models.PROTECT, related_name='note')
    time = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=500, blank=True, null=True)
  
    def __str__(self):
            return 'Note by : {} at : {}'.format(self.author.name.get().text, self.time)

