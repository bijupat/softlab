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
class User(AbstractUser) :
    pass

# // A contact party (e.g. guardian, partner, friend) for the patient##
class Contact(models.Model):
    # // The kind of relationship
    relationship = models.CharField(max_length=75, blank=True, null=True)
    # A name associated with the contact person
    #name = models.OneToOneField(name, on_delete=models.PROTECT)
    #telecom = models.ForeignKey(telecom, on_delete=models.PROTECT, related_name='Contact_Per_Telecom')
    #address =  models.ForeignKey(address, on_delete=models.PROTECT, related_name='Contact_Per_Address')
    gender = models.CharField(max_length=20, blank=True, null=True)
    #period = models.OneToOneField(period, on_delete=models.PROTECT, blank=True, null=True)
    def __str__(self):
            return 'contact  : {} is  {}'.format(self.id, self.relationship)

class Practitioner(models.Model):
    identifier = models.CharField(max_length=75, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True, default=True)
    #name = models.OneToOneField(name, on_delete=models.PROTECT, related_name='practitioner_name')
    #telecom = models.ManyToManyField(telecom, related_name='practitioner_telecom')
    gender = models.CharField(max_length=20)
    birthDate = models.DateField(blank=True, null=True)
    deceasedBoolean = models.BooleanField(blank=True, null=True, default=False)
    #address =  models.ManyToManyField(address, related_name='p                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         fractitioner_Address')
    photo = models.ImageField(blank=True, null=True)
    qualification = models.CharField(max_length=200, blank=True, null=True)
    #communication = communication()
    def __str__(self):
        return 'Practitioner id : {}'.format(self.id)



class Note(models.Model):
    author = models.ForeignKey(Practitioner, on_delete=models.PROTECT, related_name='author_note')
    time = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=500, blank=True, null=True)    
    def __str__(self):
            return 'Note by   : {} at : {}'.format(self.author, self.time)




class Patient(models.Model):
    identifier = models.CharField(max_length=75, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True, default=True)
    #name = models.ForeignKey(name, on_delete=models.PROTECT, related_name='Patient_Name')
    birthDate = models.DateField(blank=True, null=True)
    deceasedBoolean = models.BooleanField(blank=True, null=True, default=False)
    #address = models.ForeignKey(address, on_delete=models.PROTECT, related_name='Patient_Address')
    photo = models.ImageField(blank=True, null=True)
    #concact = models.ForeignKey(contact, on_delete=models.PROTECT, related_name='Patient_Contact')     
    #practitioner = models.ForeignKey(Practitioner, on_delete=models.PROTECT, related_name='Ref_by_GP',blank=True, null=True)
    

    def __str__(self):
        return 'Person name : {}'.format(self.id)  
 

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
            return 'telecom  : {} is  {}'.format(self.system, self.value)



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
            return 'name : {}'.format(self.text)


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
            return 'address : {} at : {}'.format(self.use, self.city)

class Period(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()
    patient = models.ForeignKey(Patient, on_delete=models.PROTECT, related_name='patient_period', blank=True, null=True)
    practitioner = models.ForeignKey(Practitioner, on_delete=models.PROTECT, related_name='practitioner_period', blank=True, null=True)
    #contact = models.ForeignKey(Contact, on_delete=models.PROTECT, related_name='Contact_Telecom',blank=True, null=True)
    #name = models.ForeignKey(Name, on_delete=models.PROTECT, related_name='Contact_Telecom',blank=True, null=True)
    def __str__(self):
            return 'period starts : {} and ends {}'.format(self.start, self.end)

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

class Testlist (models.Model):
    test = models.CharField(max_length=75, blank=True, null=True)
    price = models.PositiveIntegerField(blank=True, null=True)
    #sample_type = models.ManyToManyField(Sampletype,on_delete=models.PROTECT, related_name='test_sampletype', blank=True, null=True)
    pricelist_included = models.ManyToManyField(Pricelist,on_delete=models.PROTECT, related_name='test_pricelist', blank=True, null=True)
    method = models.CharField(max_length=75, blank=True, null=True)
    referenceRange_high = models.CharField(max_length=75,blank=True, null=True)
    referenceRange_low = models.CharField(max_length=75,blank=True, null=True)

    def __str__(self):
            return 'Test : {}'.format(self.test)

class Sampletype(models.Model):
    sampletype = models.CharField(max_length=75, blank=True, null=True)
    test = models.ForeignKey(Testlist, on_delete=models.PROTECT, related_name='sampletype_test' )

    def __str__(self):
            return 'SampleType : {}'.format(self.sampletype)

class Observation (models.Model):
    identifier = models.CharField(max_length=75, blank=True, null=True)
    # registered | preliminary | final | amended +
    status = models.CharField(max_length=75, blank=True, null=True, default='registered')
    entered_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='observation_entered_by', blank=True, null=True)
    verified_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='observation_verfied_by', blank=True, null=True)
    account = models.ForeignKey(Account, on_delete=models.PROTECT, related_name='observation_account', blank=True, null=True)
    timedate = models.DateTimeField(auto_now_add=True)
    test = models.ManyToManyField(Testlist, through='Encounter')
    value = models.CharField(max_length=200, blank=True, null=True)
    interpretation = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
            return 'Observation for Patient : {}'.format(self.encounter.patient.patient_name)

class Encounter(models.Model):
    identifier = models.CharField(max_length=75, blank=True, null=True)
    observation = models.ForeignKey(Observation, on_delete=models.PROTECT, related_name='encounter_observation', blank=True, null=True)
    test = models.ForeignKey(Testlist, on_delete=models.PROTECT, related_name='encounter_testlist', blank=True, null=True)
    # planned | arrived | triaged | in-progress | onleave | finished | cancelled
    status = models.CharField(max_length=75, blank=True, null=True)
    patient = models.ForeignKey(Patient, on_delete=models.PROTECT, related_name='patient_encounter', blank=True, null=True)
    practitioner = models.ForeignKey(Practitioner, on_delete=models.PROTECT, related_name='practitioner_encounter', blank=True, null=True)
    account = models.ForeignKey(Account, on_delete=models.PROTECT, related_name='account_encounter', blank=True, null=True)
    timedate = models.DateTimeField(auto_now_add=True)
        #contact = models.ForeignKey(Contact, on_delete=models.PROTECT, related_name='Contact_Telecom',blank=True, null=True)
    #name = models.ForeignKey(Name, on_delete=models.PROTECT, related_name='Contact_Telecom',blank=True, null=True)
    def __str__(self):
            return 'Encounter for Patient : {} at {}'.format(self.patient.patient_name[1].text, self.timedate)
            