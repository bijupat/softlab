from django.db import models
from django.db.models.base import Model
from django.db.models.enums import Choices
from django.contrib.auth.models import AbstractUser
from django.db.models.fields.related import OneToOneField



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
    ("M", "home"),
    ("F", "work"),
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
    gender = models.CharField(max_length=20, choices=gender)
    birthDate = models.DateField(blank=True, null=True)
    deceasedBoolean = models.BooleanField(blank=True, null=True, default=False)
    #address =  models.ManyToManyField(address, related_name='p                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         fractitioner_Address')
    photo = models.ImageField(blank=True, null=True)
    qualification = models.CharField(max_length=200, blank=True, null=True)
     #A language which may be used to communicate with the patient about his or her health.
    communication = models.CharField(max_length=25, choices=communication)
    period = models.ForeignKey(Period, on_delete=models.PROTECT, related_name='practitioner_period',blank=True, null=True)

    #communication = communication()
    def __str__(self):
        return 'Practitioner id {} name : {}'.format(self.id, self.practitioner_name.get().text)

# // A contact party (e.g. guardian, partner, friend) for the patient##
class Contact(models.Model):
    # // The kind of relationship
    relationship = models.CharField(max_length=75, blank=True, null=True, choices= Contact_relationship)
    # A name associated with the contact person
    gender = models.CharField(max_length=20, blank=True, null=True, choices=gender)
    #period = models.OneToOneField(period, on_delete=models.PROTECT, blank=True, null=True)
    def __str__(self):
        if self.contact_name.get():
            return 'Relationship {} between {}(Contact) and {}(Patient)'.format(self.relationship, self.contact_name.get().text, self.patient_contact.get().patient_name.get().text)
        else:
            return 'some error'

class Note(models.Model):
    author = models.ForeignKey(Practitioner, on_delete=models.PROTECT, related_name='author_note')
    time = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=500, blank=True, null=True)    
    def __str__(self):
            return 'Note by   : {} at : {}'.format(self.author.practitioner_name.get().text, self.time)




class Patient(models.Model):
    identifier = models.CharField(max_length=75, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True, default=True)
    #name = models.ForeignKey(name, on_delete=models.PROTECT, related_name='Patient_Name')
    birthDate = models.DateField(blank=True, null=True)
    deceasedBoolean = models.BooleanField(blank=True, null=True, default=False)
    gender = models.CharField(max_length= 10, choices=gender)
    #address = models.ForeignKey(address, on_delete=models.PROTECT, related_name='Patient_Address')
    photo = models.ImageField(blank=True, null=True)
    marital_status = models.CharField(max_length=25, choices = marital_status)
    concact = models.ForeignKey(Contact, on_delete=models.PROTECT, related_name='patient_contact',blank=True, null=True)     
    #practitioner = models.ForeignKey(Practitioner, on_delete=models.PROTECT, related_name='Ref_by_GP',blank=True, null=True)
    #A language which may be used to communicate with the patient about his or her health.
    communication = models.CharField(max_length=25, choices=communication)
    period = models.ForeignKey(Period, on_delete=models.PROTECT, related_name='patient_period',blank=True, null=True)
    class Meta:
        ordering = ["id"]

    def __str__(self):
        return 'Patient Name : {} {} having id : {}'.format(self.patient_name.get().text, self.patient_name.get().family, self.id )  
 

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
    status = models.CharField(max_length=75, blank=True, null=True)
    #patient = models.ForeignKey(Patient, on_delete=models.PROTECT, related_name='patient_account', blank=True, null=True)
    # patient, expense, depreciation
    type = models.CharField(max_length=75, blank=True, null=True)
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
class TestCategory (models.Model):
    category = models.CharField(max_length=75, blank=True, null=True)

    def __str__(self):
            return 'Category : {}'.format(self.category)

class Organization (models.Model):
    pass





#master list of observations(Testlist)
class ObservationDefinition (models.Model):
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
    # social-history/vital-signs/imaging/laboratory/procedure/survey/exam/therapy/activity
    category = models.CharField(max_length=75, blank=True, null=True) 
"""
    def __str__(self):
            return 'Test : {} by {} method with price : {}'.format(self.test, self.method, self.price)
"""
# Referance range for testlist(observationdefination)
class QualifiedInterval (models.Model):
    high = models.CharField(max_length=75, blank=True, null=True)
    low = models.CharField(max_length=75, blank=True, null=True)
    age_high = models.PositiveIntegerField(blank=True)
    age_low = models.PositiveIntegerField(blank=True)
    observationdefinition = models.ForeignKey(ObservationDefinition, on_delete=models.PROTECT, related_name='qualifiedinterval_observationdefination', blank=True, null=True)
    
    def __str__(self):
            return 'pending'

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
    timedate = models.DateTimeField(auto_now_add=True)
    #contact = models.ForeignKey(Contact, on_delete=models.PROTECT, related_name='Contact_Telecom',blank=True, null=True)
    #name = models.ForeignKey(Name, on_delete=models.PROTECT, related_name='Contact_Telecom',blank=True, null=True)
    
    class Meta:
        ordering = ["-timedate"]
    
    def __str__(self):
            return 'Encounter for Patient : {} at {}'.format(self.patient.patient_name.get().text, self.timedate)

class Observation (models.Model):
    identifier = models.CharField(max_length=75, blank=True, null=True)
    # registered | preliminary | final | amended +
    status = models.CharField(max_length=75, blank=True, null=True, default='registered')
    entered_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='observation_entered_by', blank=True, null=True)
    verified_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='observation_verfied_by', blank=True, null=True)
    #account = models.ForeignKey(Account, on_delete=models.PROTECT, related_name='observation_account', blank=True, null=True)
    timedate = models.DateTimeField(auto_now_add=True)
    test = models.ForeignKey(ObservationDefinition, related_name='observation_observationdefination', on_delete=models.PROTECT, blank=True, null=True)
    value = models.CharField(max_length=200, blank=True, null=True)
    interpretation = models.CharField(max_length=200, blank=True, null=True)
    encounter = models.ForeignKey(Encounter, on_delete=models.PROTECT, related_name='observation_encounter', blank=True, null=True)

    class Meta:
        ordering = ["-timedate"]

    """
    def __str__(self):
        if self.encounter and self.test:
            return 'Observation : {} for Patient : {} for test {}'.format(self.id, self.encounter.patient.patient_name.get().text, self.test.test)
        else:
            return 'You need to enter observation using Encounter model'
    """
class DiagnosticReport (models.Model):
    pass