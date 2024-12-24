#from xml.etree.ElementInclude import include
# from ast import Expression
from ast import mod
from django.db import models
#from django.db.models.base import Model
#from django.db.models.enums import Choices
from django.contrib.auth.models import AbstractUser
from datetime import date
#from django.db.models.fields.related import OneToOneField
#from django.contrib.postgres.fields import JSONField
from django.db.models import Sum, F , Value
from django.core.exceptions import ValidationError
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from django.db.models.functions import Concat


# master options for user lab
MASTER_OPTIONS = {
     "SAMPLE_ID_RESET" : "YEARLY"
}


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

# routine | urgent | asap | stat
servicerequest_priority=(
    ("R", "routine"),
    ("U", "urgent"),
    ("A", "asap"),
    ("S", "stat"),
    )

# Laboratory procedure| Imaging| Counselling| Education|Surgical procedure
servicerequest_category=(
    ("L", "Laboratory procedure"),
    ("I", "Imaging"),
    ("C", "Counselling"),
    ("E", "Education"),
    ("S", "Surgical procedure"),
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
    ("O", "Other(specify with name)"),
 )
obdef_or_cidef_status= (
    ("D", "draft"),
    ("A", "active"),
    ("R", "retired"),
    ("U", "unknown"),
)
# draft | issued | balanced | cancelled | entered-in-error
invoice_status = (
    ("D", "draft"),
    ("I", "issued"),
    ("B", "balanced"),
    ("C", "cancelled"),
    ("E", "entered-in-error"),
   )

# planned | billable | not-billable | aborted | billed | entered-in-error | unknown
chargeitem_status=(
    ("P", "planned"),
    ("BL", "billable"),
    ("NBL", "not-billable"),
    ("A", "aborted"),
    ("B", "billed"),
    ("E", "entered-in-error"),
    ("U", "unknown"),
)
# draft | active | on-hold | revoked | completed | entered-in-error | unknown
servicerequest_status=(
    ("D", "draft"),
    ("A", "active"),
    ("H", "on-hold"),
    ("R", "revoked"),
    ("E", "entered-in-error"),
    ("U", "unknown"),
)
# registered | partial | preliminary | final +
diagnosticreport_status=(
    ("R", "registered"),
    ("P", "partial"),
    ("PR", "preliminary"),
    ("F", "final")
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
    ("U", "Unmarried"),
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
#active | cancelled | draft | entered-in-error
PaymentReconciliation_status = (
    ("A", "Active"),
    ("C", "Cancelled"),
    ("E", "Entered-in-error"),
    ("D", "Draft"),
)
# planned | arrived | triaged | in-progress | onleave | finished | cancelled
encounter_status = (
    ("P", "planned"),
    ("A", "arrived"),
    ("T", "triaged"),
    ("IP", "in-progress"),
    ("L", "onleave"),
    ("F", "finished"),
    ("C", "cancelled"),

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
    ("P", "Patient"),
    ("C", "Expence"),
    ("T", "Depreciation"),
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

appointment_status=(
    ("P", "proposed"),
    ("PE", "pending"),
    ("B", "booked"),
    ("A", "arrived"),
    ("F", "fulfilled"),
    ("C", "cancelled"),
    ("N", "noshow"),
    ("E", "entered-in-error"),
    ("CH", "checked-in"),
    ("W", "waitlist"),
)


sample_status=(
    ("CO", "collected"),
    ("RC", "received"),
    ("RJ", "rejected"),
    ("S", "stored"),
    ("D", "discarded"),
    ("CA", "cancelled"),
    ("P", "pending"),


)

class User(AbstractUser) :
    pass

class Period(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()

    def __str__(self):
            return 'Period for Starts :{}/{}/{} and Ends :{}/{}/{} (dd/mm/yyyy)'.format(self.start.day, self.start.month, self.start.year, self.end.day, self.end.month, self.end.year)

class Name(models.Model):
    # // usual | official | temp | nickname | anonymous | old | maiden
    use = models.CharField(max_length=7, blank=True, null=True, choices =Name_use, default="U")
    # // Parts that come before the name
    prefix = models.CharField(max_length=75, blank=True, null=True)
    # // Given names (not always 'first'). Includes middle names
    given = models.CharField(max_length=75, blank=True, null=True)
    # // Family name (often called 'Surname')
    family = models.CharField(max_length=75, blank=True, null=True)
    # // Parts that come after the name
    suffix = models.CharField(max_length=75, blank=True, null=True)
    # // Text representation of the full name by generated field
    text = models.GeneratedField(
        expression=Concat('given', Value(' '), 'family'),
        output_field = models.CharField(max_length=256,),
        db_persist= True,
        )
    #Generic Foreign key for multiple content_types
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")

    class Meta:
        indexes = [
            models.Index(fields=["content_type", "object_id"]),
        ]

    def __str__(self):
        return f'{self.text}'


"""    def serialize(self):
        #if name if for patient it will retun filled dict
        if self.patient:
            mobno = ""
            for t in self.patient.telecom.all():
                if t.use == "M":
                    mobno = t.value
            return{
                "fname": self.given,
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
"""



class Telecom(models.Model):
    # phone | fax | email | pager | url | sms | other
    system = models.CharField(max_length=10, choices= Telecom_system)
    # // home | work | temp | old | mobile - purpose of this contact point
    use = models.CharField(max_length=10, choices=Telecom_use)
    # The actual contact point details
    value = models.CharField(max_length=75,)
    # // Specify preferred order of use (1 = highest)
    rank = models.IntegerField(blank=True, null=True)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")

    class Meta:
        indexes = [
            models.Index(fields=["content_type", "object_id"]),
        ]


    def __str__(self):
        return 'Telecom : {}/{}: {}'.format(self.get_system_display(), self.get_use_display(), self.value)

class Address(models.Model):
    # // home | work | temp | old | billing - purpose of this address
    use = models.CharField(max_length=75, choices=Address_use)
    # // Text representation of the address
    text = models.CharField(max_length=250, blank=True, null=True)
    # // Street name, number, direction & P.O. Box etc.
    line = models.CharField(max_length=250, blank=True, null=True)
    # // Name of city, town etc.
    city = models.CharField(max_length=75, default="Ahmedabad",blank=True, null=True)
    district = models.CharField(max_length=75, default="Ahmedabad", blank=True, null=True)
    state = models.CharField(max_length=250, default="Gujarat",blank=True, null=True)
    postalcode = models.CharField(max_length=250,blank=True, null=True)
    country = models.CharField(max_length=250, default="India",blank=True, null=True)


    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")

    class Meta:
        indexes = [
            models.Index(fields=["content_type", "object_id"]),
        ]
    def __str__(self):
         return f'{self.content_type}'


class Contact(models.Model):
    # // The kind of relationship
    relationship = models.CharField(max_length=75, blank=True, null=True, choices= Contact_relationship)
    # A name associated with the contact person
    gender = models.CharField(max_length=20, blank=True, null=True, choices=gender)
    #period = models.OneToOneField(period, on_delete=models.PROTECT, blank=True, null=True)
    names = GenericRelation(Name, related_query_name="contact")
    telecoms = GenericRelation(Telecom, related_query_name="contact")
    address = GenericRelation(Address, related_query_name="contact")

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")

    class Meta:
        indexes = [
            models.Index(fields=["content_type", "object_id"]),
        ]

    def __str__(self):
        try:
            return 'Contact id-{}: Relationship {} between {}(Contact) and {}(Patient)'.format(self.id, self.get_relationship_display(), self.names.get().text, self.patient.get().names.get().text)
        except:
            return 'some error'
        
class Patient(models.Model):
    identifier = models.CharField(max_length=75, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True, default=True)
    birthdate = models.DateField(blank=True, null=True)
    deceasedboolean = models.BooleanField(blank=True, null=True, default=False)
    gender = models.CharField(max_length= 10, choices=gender,blank=True, null=True)
    photo = models.ImageField(blank=True, null=True)
    marital_status = models.CharField(max_length=25, choices = marital_status,blank=True, null=True)
    communication = models.CharField(max_length=25, choices=communication, blank=True, null=True)
    period = models.ForeignKey(Period, on_delete=models.PROTECT, related_name='patients',blank=True, null=True)
    names = GenericRelation(Name, related_query_name="patient")
    telecoms = GenericRelation(Telecom, related_query_name="patient")
    address = GenericRelation(Address, related_query_name="patient")
    contact = GenericRelation(Contact, related_query_name="patient")
    class Meta:
        ordering = ["id"]
    # implenting age field to be calculated from birth date
    @property
    def age(self):
        if self.birthdate: 
            return date.today().year - self.birthdate.year

    #Do Not use this get_*  properties as it causes repeated SQL in prefetch related 
    # only for admin site
    # instead use for in in template to get names. telecoms etcs
    # defining method that returns usual name
    def get_usual_name(self):
        try:
            return self.names.filter(use="U")[0].text or ""
        except:
            return ""
    # defining method that returns PHONE mobile no
    def get_mobile(self):
        try:
            return self.telecoms.filter(system= "P", use="M").order_by('rank')[0].value or ""
        except:
            return ""
    # defining method that returns e mail(ANY USE)
    def get_email(self):
        try:
            return self.telecoms.filter(system= "E").order_by('rank')[0].value 
        except:
            return ""
    

    def __str__(self):  
        # return f'{self.names.filter(use="U")[0].text or ""}'
        return f"{self.id}"

class Practitioner(models.Model):
    identifier = models.CharField(max_length=75, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True, default=True)
    gender = models.CharField(max_length=20, choices=gender,blank=True, null=True)
    birthDate = models.DateField(blank=True, null=True)
    deceasedBoolean = models.BooleanField(blank=True, null=True, default=False)
    photo = models.ImageField(blank=True, null=True)
    qualification = models.CharField(max_length=200, blank=True, null=True)
     #A language which may be used to communicate with the patient about his or her health.
    communication = models.CharField(max_length=25, choices=communication, blank=True, null=True)
    period = models.ForeignKey(Period, on_delete=models.PROTECT, related_name='practitioners',blank=True, null=True)
    names = GenericRelation(Name, related_query_name="practitioner")
    telecoms = GenericRelation(Telecom, related_query_name="practitioner")
    address = GenericRelation(Address, related_query_name="practitioner")

    @property
    def fullname(self):
        try:
            return 'Dr {} {}'.format(self.names.get().given.title(), self.names.get().family.title())
        except:
            pass
        finally:
            try:
                return 'Dr {}'.format( self.names.get().given.title()) 
            except:
                return f'Practitioner id {self.id}'
        
    def __str__(self):
        return self.fullname


class Note(models.Model):
    author = models.ForeignKey(Practitioner, on_delete=models.PROTECT, related_name='notes')
    time = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=500, blank=True, null=True)
  
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")

    class Meta:
        indexes = [
            models.Index(fields=["content_type", "object_id"]),
        ]

  
    def __str__(self):
            return 'Note by : {} at : {}'.format(self.author.names.get().text, self.time)
    

class Organization (models.Model):
    identifier = models.CharField(max_length=75, blank=True, null=True)
    # Whether the organization's record is still in active use
    active = models.BooleanField(blank=True, null=True, default=True)
    #Name used for the organization
    name = models.CharField(max_length=75, blank=True, null=True)
    # A list of alternate names that the organization is known as, or was known as in the past
    alias = models.CharField(max_length=75, blank=True, null=True)
    # Contact for the organization for a certain purpose 
    # contact = models.ForeignKey(Contact, on_delete=models.PROTECT, related_name='organizations',blank=True, null=True)


    def __str__(self):
            return 'Organization  : {}'.format(self.name)



#master data class
class Pricelist(models.Model):
    pricelist = models.CharField(max_length=75, blank=True, null=True)
    #remove blank = true and null = true in production version
    # account = models.ForeignKey(Account, on_delete=models.PROTECT, related_name='pricelist',blank=True, null=True)
    category = models.CharField(max_length=75, blank=True, null=True)
    notes = GenericRelation(Note, related_query_name="note")

    def __str__(self):
            return 'Pricelist : {}'.format(self.pricelist)
    
class Account (models.Model):
    identifier = models.CharField(max_length=75, blank=True, null=True)
    # active | inactive | entered-in-error | on-hold | unknown
    status = models.CharField(max_length=75, blank=True, null=True, choices= Account_status, default='A')
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
    pricelist = models.ForeignKey(Pricelist, on_delete=models.PROTECT, related_name='accounts',blank=True, null=True)
    # contact
    contact = models.ForeignKey(Contact, on_delete=models.PROTECT, related_name='accounts',blank=True, null=True)
    notes = GenericRelation(Note, related_query_name="note")

    def __str__(self):
            return '{}'.format(self.name)

class SpecimenType(models.Model):
    specimentype = models.CharField(max_length=75, blank=True, null=True)

    def __str__(self):
            return f'{self.specimentype}'



class TestCategory(models.Model):
    category = models.CharField(max_length=75, blank=True, null=True)

    def __str__(self):
            return 'Category : {}'.format(self.category)

  

    
# Master list of depatement like biochem, hemat, histo
class Department(models.Model):
    pass

class Equipments(models.Model):
    pass




#master list of observations(Testlist)
class ObservationDefinition(models.Model):
    # use loinic Consumer Name if possible
    test = models.CharField(max_length=500, blank=True, null=True)
    # general name usded in routine practice
    alias = models.CharField(max_length=75, blank=True, null=True)
    # name used in SMS field
    # draft | active | retired | unknown
    status = models.CharField(max_length=20, blank=True, null=True, choices=obdef_or_cidef_status, default = "A")
    alias_sms = models.CharField(max_length=75, blank=True, null=True)  
    method = models.CharField(max_length=75, blank=True, null=True)
    category = models.ForeignKey(TestCategory, on_delete=models.PROTECT, related_name='observationdefinations', blank=True, null=True)
    unit = models.CharField(max_length=75, blank=True, null=True)
    # option fields in observation defination, implemented as set or other method-- all options in one field
    # default value for the observatoin like "Nil" in Urine Sugar
    default_value = models.CharField(max_length=1000, blank=True, null=True)
    # select option for html
    options = models.CharField(max_length=5000, blank=True, null=True)
    #equipment used for the test
    equipment = models.ForeignKey(Equipments, on_delete=models.PROTECT, related_name='observationdefinations', blank=True, null=True)
    #test code to communicate with equipment for interphase
    equipmentcode = models.CharField(max_length=75, blank=True, null=True)
    loinc_code = models.CharField(max_length=75, blank=True, null=True)
    #The low and high values determining the interval. There may be only one of the two
    # social-history/vital-signs/imaging/laboratory/procedure/survey/exam/therapy/activity
    # Specimentype Required for this chargeitem/test/report
    specimentypes = models.ManyToManyField(SpecimenType, related_name='observationdefinations', blank=True,)
    # note specific to the observation
    note = models.CharField(max_length=1000, blank=True, null=True)
    # which department in lab as per department define in model ie biochem, histo etc
    dept = models.ForeignKey(Department,  on_delete=models.PROTECT, related_name='observationdefinations', blank=True, null=True)
    # TAT for the field
    tat = models.SmallIntegerField(blank=True, null=True)
    is_calculated = models.BooleanField(blank=True, null=True, default=False)
    # formula if calculated test
    formula = models.CharField(max_length=200, blank=True, null=True)
    # Validation Rule 
    vrule = models.CharField(max_length=200, blank=True, null=True)
    # Validation message if not validated
    vmsg = models.CharField(max_length=200, blank=True, null=True)
    # Validation if must ?.
    vrulemust = models.BooleanField(blank=True, null=True,default=True)
    #The low and high values determining the interval. There may be only one of the two
    # it will be implemented from qulified interval class as foreign  key
    class Meta:
        ordering = ["test"]
    def __str__(self):
            return '{} in {} by {}'.format(self.test, self.id, self.method)

# Referance range for testlist(observationdefination)
class QualifiedInterval(models.Model):    
    high = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    low = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    text_as_normal =  models.CharField(max_length=500, blank=True, null=True)
    # category can be reference | critical | absolute
    category = models.CharField(max_length=10, choices=qualifiedInterval_category, default="R")
    # highest age for the qualified interval EXCLUDING it
    age_high = models.PositiveIntegerField(blank=True, default=150)
    # Lowest  age for the qualified interval INCLUDING it 
    age_low = models.PositiveIntegerField(blank=True, default=0)
    gender = models.CharField(max_length=20, choices=gender,blank=True, null=True)
    observationdefinition = models.ForeignKey(ObservationDefinition, on_delete=models.PROTECT, related_name='qualifiedintervals', blank=True, null=True)
    gestationalAge = models.CharField(max_length=50, blank=True, null=True)
    #Text based condition for which the reference range is valid.
    condition = models.CharField(max_length=75, blank=True, null=True)
    def __str__(self):
            return 'For {} as {} age {} to {} / {}'.format(self.observationdefinition, self.category, self.age_low, self.age_high,  self.gender)

class Invoice(models.Model):
    identifier = models.CharField(max_length=75, blank=True, null=True)
    # draft | issued | balanced | cancelled | entered-in-error
    status = models.CharField(max_length=75, choices=invoice_status, blank=True, null=True, default='I')
    cancelled_reason = models.CharField(max_length=200, blank=True, null=True)
    # Recipient(s) of goods and services
    subject = models.ForeignKey(Patient, on_delete=models.PROTECT, related_name='invoices', blank=True, null=True)
    # Recipient of this invoice
    recipient = models.ForeignKey(Organization, on_delete=models.PROTECT, related_name='invoices', blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    # Participant in creation of this Invoice
    participant = models.ForeignKey(Practitioner, on_delete=models.PROTECT, related_name='invoices', blank=True, null=True)
    account = models.ForeignKey(Account, on_delete=models.PROTECT, related_name='invoices', blank=True, null=True)
    discount = models.PositiveIntegerField(blank=True, null=True)
    paymentTerms = models.CharField(max_length=200, blank=True, null=True)
    # Comments made about the invoice by the issuer, subject, or other participants.
    notes = GenericRelation(Note, related_query_name="note")

    """
    payment property returns dict with details of calculated vaues of payment
    """
    @property
    def payments(self):
        dict = {}
        total = 0
        for e in self.encounter.all():
            chargeItems = ChargeItem.objects.filter(context=e)
            for c in chargeItems:
                total += c.priceOverride or 0
        dict['totalGross'] = total
        paid = 0
        for p in self.paymentreconciliation.all():
            paid += p.paymentAmount or 0
        dict['paid'] = paid
        dict['due'] = total - (paid + self.discount)
        dict['totalnet'] = total-self.discount
        return dict      


    def __str__(self):
        return f'Inovoice id {self.id} for {self.subject}'

class Device(models.Model):
    pass

    def __str__(self):
        return f'Test : '

#master data class for headings of priceitem definations
class Headings(models.Model):
    heading = models.CharField(max_length=75, blank=True, null=True)
    notes = GenericRelation(Note, related_query_name="note")
    
    def __str__(self):
            return '{}'.format(self.heading)
    
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
    includes = models.ManyToManyField("self", blank=True,)
    #Completed or terminated request(s) whose function is taken by this new request
    replaces = models.ManyToManyField("self", blank=True,)
    # draft | active | retired | unknown
    status = models.CharField(max_length=20, blank=True, null=True, choices=obdef_or_cidef_status, default = "A")
    prices = models.ManyToManyField(Pricelist, through='Price', related_name='chargeitemdefs')
    # For testing purposes, not real usage
    experimental = models.BooleanField(blank=True, null=True, default=False)
    # is it needed to be printed in receipt ?
    print_in_receipt = models.BooleanField(blank=True, null=True, default=True)
    # is it individula test or profiel ?
    is_profile = models.BooleanField(blank=True, null=True, default=False)
    # observations(test) included in this charge item
    observations = models.ManyToManyField(ObservationDefinition, blank=True, related_name='chargeitemdefs')
    # heading to the report print like Hemogram / Liver function test implemented to whole  report
    # TAT for the field
    tat = models.SmallIntegerField(blank=True, null=True)
    heading = models.ForeignKey(Headings, on_delete=models.PROTECT, related_name='chargeitemdefs', blank=True, null=True)
    category = models.CharField(max_length=20, blank=True, null=True, choices=ObservationDefinition_category, default="L")
    # date on which first approved 
    approvalDate = models.DateTimeField(blank=True, null=True)
    #Date last changed
    lastReviewDate = models.DateTimeField(blank=True, null=True)
    effectivePeriod = models.ForeignKey(Period,blank=True, null=True, related_name='chargeitemdefs', on_delete=models.PROTECT)
    #Monetary amount associated with this
    # value = models.PositiveIntegerField(blank=True, null=True)
    specimentypes = models.ManyToManyField(SpecimenType, related_name='chargeitemdefs', blank=True)
    # which department in lab as per department define in model ie biochem, histo etc
    dept = models.ForeignKey(Department,  on_delete=models.PROTECT, related_name='chargeitemdefs', blank=True, null=True)
    # if test is outsourced 
    outsourced_to = models.ForeignKey(Organization, on_delete=models.PROTECT, related_name='chargeitemdefs', blank=True, null=True)
    # use to filter price list in views.py for observations
    # pricelist_included = models.ManyToManyField(Pricelist, related_name='chargeitemdef', blank=True)
    # Note for specific  test like double marker applies to whole report
    Note = models.CharField(max_length=75,blank=True, null=True)
    # Product/equipment charged or used
    product = models.ForeignKey(Device, on_delete=models.CASCADE, related_name='chargeitemdefs', null=True, blank=True)
    # ordering of obseration if more than one observatin involved
    orderBy= models.SmallIntegerField(blank=True, null=True) 
    def __str__(self):
        return self.title  

class Price(models.Model):
    chargeitemdef = models.ForeignKey(ChargeItemDefinition, on_delete=models.CASCADE, related_name='price_s', null=True, blank=True)
    pricelist = models.ForeignKey(Pricelist, on_delete=models.CASCADE,related_name='prices',null=True, blank=True)
    price = models.DecimalField(max_digits=9, decimal_places=2)

    def clean(self):
        duplicate = Price.objects.exclude(pk=self.pk).filter(chargeitemdef_id=self.chargeitemdef_id, pricelist_id=self.pricelist_id).exists()
        if duplicate:
            raise ValidationError('The price for this chargeitem with this pricelist already exists')
        return super().clean()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['chargeitemdef', 'pricelist'], name='price_for_chargeitemdef_asper_pricelist')
        ]
    def __str__(self):
        return f'{self.chargeitemdef.title} ({self.pricelist.pricelist}) rs : {self.price}'


class Encounter(models.Model):
    sample_id = models.IntegerField(default=0)
    identifier = models.CharField(max_length=75, blank=True, null=True)
    tests = models.ManyToManyField(ChargeItemDefinition, through='ChargeItem', related_name='encounter')
    #observations = models.ManyToManyField(ObservationDefinition, through='Observation', related_name='encounter')
    # planned | arrived | triaged | in-progress | onleave | finished | cancelled
    status = models.CharField(max_length=75, choices= encounter_status, default='IP', blank=True, null=True)
    patient = models.ForeignKey(Patient, on_delete=models.PROTECT, related_name='encounters', blank=True, null=True)
    practitioner = models.ForeignKey(Practitioner, on_delete=models.PROTECT, related_name='encounters', blank=True, null=True)
    account = models.ForeignKey(Account, on_delete=models.PROTECT, related_name='encounters', blank=True, null=True)
    # one invoice can be created for more than one encounter
    invoice = models.ForeignKey(Invoice, on_delete=models.PROTECT, related_name='encounters', blank=True, null=True)
    timedate = models.DateTimeField(auto_now_add=True)
    # if urgent  reporting required 
    urgent=  models.BooleanField(default=False)  # Field name made lowercase.
    notes = GenericRelation(Note, related_query_name="note")
    # override default save method to autoincrement sample_id
    def save(self, *args, **kwargs):
        # This means that the model isn't saved to the database yet
        if self._state.adding:
            # Get the maximum display_id value from the database
            last_sample_id = Encounter.objects.all().aggregate(largest=models.Max('sample_id'))['largest']
            # aggregate can return None! Check it first.
            # If it isn't none, just use the last ID specified (which should be the greatest) and add one to it
            if last_sample_id is not None:
                self.sample_id = last_sample_id + 1      
        super(Encounter, self).save(*args, **kwargs)

    class Meta:
        ordering = ["timedate"]
    
    def __str__(self):
            return 'Encounter id {} for Patient : {} at {}'.format(self.id, self.patient.get_usual_name(), self.timedate)

#instance of individual samples
class Sample(models.Model):
    specimentype = models.ForeignKey(SpecimenType, on_delete=models.PROTECT, related_name='sample',blank=True, null=True)
    encounter = models.ForeignKey(Encounter, on_delete=models.PROTECT, related_name='sample',blank=True, null=True)
    status = models.CharField(max_length=75, choices= sample_status, blank=True, null=True, default='P')
    
    def __str__(self):
            return 'SID {} type : {} status {}'.format(self.encounter.sample_id, self.specimentype.specimentype, self.get_status_display())



class ChargeItem(models.Model):
    identifier = models.CharField(max_length=75, blank=True, null=True)
    # Resource defining the code of this ChargeItem
    definitionCanonical = models.ForeignKey(ChargeItemDefinition, on_delete=models.CASCADE, null=True, blank=True, related_name='chargeitem')
    # planned | billable | not-billable | aborted | billed | entered-in-error | unknown
    status = models.CharField(max_length=75, choices= chargeitem_status, blank=True, null=True, default='B')
    #Part of referenced ChargeItem
    partOf = models.ForeignKey("self", on_delete=models.CASCADE, related_name='partof', null=True, blank=True)
    # Individual service was done for/to
    subject = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='chargeitems', null=True, blank=True)
    # Encounter / Episode associated with event
    context = models.ForeignKey(Encounter, on_delete=models.CASCADE, related_name='chargeitems', null=True, blank=True)
    # When the charged service was applied
    occurrenceDateTime = models.DateTimeField(auto_now_add=True)
    # Price overriding first time as default from chargeitemdefination.value
    priceOverride = models.PositiveIntegerField(blank=True, null=True)
    # Reason for overriding if done aftert first entry the list price/factor
    overrideReason = models.CharField(max_length=200, blank=True, null=True, default="Registration")
    #price override by 
    priceoverrideby = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chargeitems_priceoverriden', null=True, blank=True)
    # Individual who was entering
    enterer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='chargeitems_entered', null=True, blank=True)
    # Which rendered service is being charged?
    #service = models.ForeignKey(DiagnosticReport, on_delete=models.CASCADE, related_name='chargeitem_diagnosticreport', null=True, blank=True)
    # heading to the report print like Hemogram / Liver function test implemented to whole  report : to be copied from chargeitem Defination

    #heading = models.CharField(max_length=75, blank=True, null=True)

    observations = models.ManyToManyField(ObservationDefinition, through='Observation', related_name='chargeitems')

    # Account to place this charge
    account = models.ForeignKey(Account, on_delete=models.PROTECT, related_name='ChargeItems', blank=True, null=True)
    # copies  from charge item defination but open for edit if desired
    notes = GenericRelation(Note, related_query_name="note")

    def is_all_atleat_final(self):
        obs = Observation.objects.filter(chargeitem = self)
        for ob in obs:
            if ob.status == "P" or ob.status == "R":
                return False
        return True
    
    # update priceOverride from Price table finidng price for chargeitem in pricelist
    def update_price(self):
        self.priceOverride = Price.objects.filter(chargeitemdef = self.definitionCanonical, pricelist=self.account.pricelist).get().price

    def __str__(self):
        return f' id : {self.id} Test : {self.definitionCanonical} for Enc : {self.context.id}'

class Observation(models.Model):
    identifier = models.CharField(max_length=75, blank=True, null=True)
    # registered | preliminary | final | amended + |informed | delivered
    status = models.CharField(max_length=75, blank=True, null=True, default='R',  choices= Observation_status)
    # change staus to preliminary if report entered by operator(entered in pplus)
    prelimnary_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='prelimnary_observations', blank=True, null=True)
    # changes to final if reported  is verified by pathologist(verified in pplus)
    final_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='final_observations', blank=True, null=True)
    # changes to informed if reported  is informed by user
    informed_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='informed_observations', blank=True, null=True)
    # changes to dlivered if delivered
    delivered_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='delivered_observations', blank=True, null=True)
    # changes to amended if amended
    amended_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='amended_observations', blank=True, null=True)
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
    testfield = models.ForeignKey(ObservationDefinition, related_name='observations', on_delete=models.PROTECT, blank=True, null=True)
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
    notes = GenericRelation(Note, related_query_name="note")

    def populate_fm_obdef(self):
        self.unit = self.testfield.unit or "" 
        self.note = self.testfield.note or ""
        refints = self.testfield.qualifiedintervals.all()
        self.high, self.low = "", ""
        for refint in refints:
            # IF qualified interval category ref interval
            if refint.category == "R":                
                # if text_as_normal enter use it pupulate high
                if refint.text_as_normal:
                    self.high, self.low = refint.text_as_normal, ""
                # elif text_normal empty select ref int depending on Patient age and Gender
                elif self.chargeitem.subject.age in range(int(refint.age_low), int(refint.age_high)) and self.chargeitem.subject.gender == refint.gender:
                    self.high, self. low = refint.high, refint.low
        self.save()

    @property
    def refint(self):
        if self.low:
            return f"{self.low} - {self.high}"
        else:
            return {self.high}

    class Meta:
        ordering = ["-timedate"]
    
    def __str__(self):
        if self.chargeitem and self.testfield:
            return 'Observation : {} for Patient : {} for test {} on Encounter id : {}'.format(self.id, self.chargeitem.context.patient.names.get().text, self.testfield.test, self.chargeitem.context.id)
        else:
            return 'You need to enter observation using Encounter model'

class Media(models.Model):
    pass

class ServiceRequet(models.Model):
    replaces = models.ForeignKey("self", on_delete=models.PROTECT, related_name='replaced_by', blank=True, null=True)
    # draft | active | on-hold | revoked | completed | entered-in-error | unknown
    status = models.CharField(max_length=75,  choices= servicerequest_status, blank=True, null=True, default='A')
    # Laboratory procedure| Imaging| Counselling| Education|Surgical procedure
    category = models.CharField(max_length=20, blank=True, null=True, choices=servicerequest_category, default="L")
    # routine | urgent | asap | stat
    priority = models.CharField(max_length=20, blank=True, null=True, choices=servicerequest_priority, default="R")
    doNotPerform = models.BooleanField(blank=True, null=True, default=False)
    #  Procedure Codes (SNOMED CT)
    code = models.CharField(max_length=75, blank=True, null=True, )
    occurrenceDateTime = models.DateTimeField(auto_now_add=True)
    # Date request signed
    tests = models.ManyToManyField(ChargeItemDefinition, related_name='ServiceRequests', blank=True)
    practitioner = models.ForeignKey(Practitioner, on_delete=models.PROTECT, related_name='ServiceRequests', blank=True, null=True)

    authoredOn = models.DateTimeField(blank=True, null=True,)
    encounter = models.OneToOneField(Encounter, on_delete=models.CASCADE, related_name='ServiceRequest', null=True, blank=True)
    subject = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='ServiceRequests', null=True, blank=True)
    requester = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ServiceRequests', blank=True, null=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='ServiceRequests', blank=True, null=True)

    notes = GenericRelation(Note, related_query_name="note")
    specimentypes = models.ManyToManyField(SpecimenType,  related_name='ServiceRequests', blank=True)
    patientInstruction = models.CharField(max_length=1000, blank=True, null=True)

    def __str__(self):
        return f'Service Request id {self.id}'

 

class DiagnosticReport (models.Model):
    identifier = models.CharField(max_length=75, blank=True, null=True)
    basedOn = models.ForeignKey(ServiceRequet, on_delete=models.CASCADE, related_name='DiagnosticReports', null=True, blank=True)
    # registered | partial | preliminary | final +
    status = models.CharField(max_length=75,  choices= diagnosticreport_status, blank=True, null=True, default='R')
    # https://www.hl7.org/fhir/valueset-diagnostic-service-sections.html
    category = models.CharField(max_length=75, blank=True, null=True)
    #Name/Code lionic for this diagnostic report
    code = models.CharField(max_length=75, blank=True, null=True)
    subject = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='DiagnosticReports', null=True, blank=True)
    encounter = models.ForeignKey(Encounter, on_delete=models.CASCADE, related_name='DiagnosticReports', null=True, blank=True)
    effectiveDateTime = models.DateTimeField(blank=True, null=True)
    # person Responsible Diagnostic Service equivalent to ENTERED by in pplus
    performer = models.ForeignKey(User, on_delete=models.PROTECT, related_name='DiagnosticReports_performed', blank=True, null=True)
    # person Responsible Diagnostic Service equivalent to verified by in pplus
    resultsInterpreter = models.ForeignKey(User, on_delete=models.PROTECT, related_name='DiagnosticReports_resultinterpreted', blank=True, null=True)
    # specimentype this report is based on
    specimentypes = models.ManyToManyField(SpecimenType,  related_name='DiagnosticReports', blank=True)
    result = models.ForeignKey(Observation, on_delete=models.PROTECT, related_name='DiagnosticReports', blank=True, null=True)
    media_link = models.ForeignKey(Media, on_delete=models.PROTECT, related_name='DiagnosticReports', blank=True, null=True)
    conclusion = models.CharField(max_length=75, blank=True, null=True, default='registered')
    notes = GenericRelation(Note, related_query_name="note")
    # Entire report as issued Rich text representation of the entire result as issued by the diagnostic service 
    # can be equivalent to layout in pplus rtf data
    presentedForm = models.CharField(max_length=1000, blank=True, null=True)
    def __str__(self):
        return f'{self.code}'




class PaymentReconciliation(models.Model):
    identifier = models.CharField(max_length=75, blank=True, null=True)
    #  active | cancelled | draft | entered-in-error
    status = models.CharField(max_length=75, blank=True, null=True, default='A', choices=PaymentReconciliation_status)
    # Creation date The date when the resource was created.
    created = models.DateTimeField(auto_now_add=True)
    # Need to identify the party resonsible for the payment and this resource.
    payment_issuer = models.ForeignKey(Organization, on_delete=models.PROTECT, related_name='payments', blank=True, null=True)
    # Reference to requesting resource (Invoice)
    request = models.ForeignKey(Invoice, on_delete=models.PROTECT, related_name='payments', blank=True, null=True)
    #payment received by user
    received_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='payments_received', blank=True, null=True)
    # When payment issued
    paymentDate = models.DateField(auto_now_add=True)
    # Total amount of Payment Total payment amount as indicated on the financial instrument.
    paymentAmount = models.PositiveIntegerField(blank=True, null=True)
    # The period of time for which payments have been gathered into this bulk payment for settlement.(For Periodic Accounts )
    period = models.ForeignKey(Period, on_delete=models.PROTECT, related_name='payments',blank=True, null=True)

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




class Slot(models.Model):
    pass
    def __str__(self):
            return 'Slot id {}'.format(self.id)
    

class AppointmentResponse(models.Model):
    identifier = models.CharField(max_length=75, blank=True, null=True)
    def __str__(self):
            return 'AppointmentResponse id {}'.format(self.id)
    

# last element (CODEBEL CONCEPT) of Resource Appointment in FHIR VER 5 That defines recurrent appointment
class RecurrenceTemplate(models.Model):
    identifier = models.CharField(max_length=75, blank=True, null=True)

    def __str__(self):
            return 'RecurrenceTemplate id {}'.format(self.id)
    
class Appointment(models.Model):
    #  proposed | pending | booked | arrived | fulfilled | cancelled | noshow | entered-in-error | checked-in | waitlist|
    status = models.CharField(max_length=75, blank=True, null=True, default='B', choices=appointment_status)
    cancelationreason = models.CharField(max_length=75, blank=True, null=True)
    #The specialty of a practitioner that would be required to perform the service requested in this appointment eg ecg, mer 
    specialty =  models.CharField(max_length=75, blank=True, null=True)
    # Used to make informed decisions if needing to re-prioritize
    priority = models.BooleanField(blank=True, null=True, default=False)
    # Shown on a subject line in a meeting request, or appointment list
    description = models.CharField(max_length=75, blank=True, null=True)
    replaces = models.ForeignKey("self", on_delete=models.PROTECT, related_name='replaced_by', blank=True, null=True)
    #Connection details of a virtual service (e.g. conference call)
    virtualService = models.CharField(max_length=75, blank=True, null=True)
    #The previous appointment in a series
    previousappointment = models.ForeignKey("self", on_delete=models.PROTECT, related_name='originalappointments', blank=True, null=True)
    #The originating appointment in a recurring set of appointments
    originatingappointment = models.ForeignKey("self", on_delete=models.PROTECT, related_name='previousappointments', blank=True, null=True)
    # When appointment is to take place 
    start = models.DateTimeField(blank=True, null=True)
    # When appointment is to conclude     
    end = models.DateTimeField(blank=True, null=True)
    #The slots that this appointment is filling
    slot = models.ForeignKey(Slot, on_delete=models.PROTECT, related_name='appointments', blank=True, null=True)
    account = models.ForeignKey(Account, on_delete=models.PROTECT, related_name='appointments', blank=True, null=True)
    # The date that this appointment was initially created
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    # the user who creatd appointment
    created_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='appointments_created', blank=True, null=True)
    # When the appointment was cancelled
    cancellationdate = models.DateTimeField(blank=True, null=True)
    # Detailed information and instructions for the patient
    patientinstruction = models.CharField(max_length=75, blank=True, null=True)
    subject = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='appointments', null=True, blank=True)
    #users needed during appointment
    participants = models.ManyToManyField(User, related_name='appointments_participated', blank=True)
    # Indicates that this appointment varies from a recurrence pattern
    occurrencechanged = models.BooleanField(blank=True, null=True, default=False)
    recurrencetemplate = models.ForeignKey(RecurrenceTemplate, on_delete=models.CASCADE, related_name='appointments', null=True, blank=True)
    # indicate organisation (TPA) associated with patient
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE, related_name='appointments', null=True, blank=True)
    tests = models.ManyToManyField(ChargeItemDefinition, related_name = 'appointments')
    def __str__(self):
            return 'Appointment for : {} at : {}'.format(self.subject, self.start)
    


