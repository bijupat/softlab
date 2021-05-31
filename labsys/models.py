from django.db import models
from django.db.models.enums import Choices


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
    #name = models.OneToOneField(name, on_delete=models.PROTECT, related_name='Practitioner_name')
    #telecom = models.ManyToManyField(telecom, related_name='Practitioner_telecom')
    gender = models.CharField(max_length=20)
    birthDate = models.DateField(blank=True, null=True)
    deceasedBoolean = models.BooleanField(blank=True, null=True, default=False)
    #address =  models.ManyToManyField(address, related_name='Practitioner_Address')
    photo = models.ImageField(blank=True, null=True)
    qualification = models.CharField(max_length=200, blank=True, null=True)
    #communication = communication()
    def __str__(self):
        return 'Practitioner id : {}'.format(self.id)



class Note(models.Model):
    author = models.ForeignKey(Practitioner, on_delete=models.PROTECT, related_name='Note_by')
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
    practitioner = models.ForeignKey(Practitioner, on_delete=models.PROTECT, related_name='Ref_by_GP',blank=True, null=True)
    

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
    patient = models.ForeignKey(Patient, on_delete=models.PROTECT, related_name='Patient_Telecom', blank=True, null=True)
    practitioner = models.ForeignKey(Practitioner, on_delete=models.PROTECT, related_name='Practitioner_Telecom', blank=True, null=True)
    contact = models.ForeignKey(Contact, on_delete=models.PROTECT, related_name='Contact_Telecom',blank=True, null=True)



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
    patient = models.ForeignKey(Patient, on_delete=models.PROTECT, related_name='Patient_Name', blank=True, null=True)
    practitioner = models.ForeignKey(Practitioner, on_delete=models.PROTECT, related_name='Practitioner_Name', blank=True, null=True)
    contact = models.ForeignKey(Contact, on_delete=models.PROTECT, related_name='Contact_Name',blank=True, null=True)
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
    patient = models.ForeignKey(Patient, on_delete=models.PROTECT, related_name='Patient_Address', blank=True, null=True)
    practitioner = models.ForeignKey(Practitioner, on_delete=models.PROTECT, related_name='Practitioner_Address', blank=True, null=True)
    contact = models.ForeignKey(Contact, on_delete=models.PROTECT, related_name='Contact_Address',blank=True, null=True)
    # Time period when name was/is in use
    #period = models.OneToOneField(period, on_delete=models.PROTECT, blank=True, null=True)
    def __str__(self):
            return 'address : {} at : {}'.format(self.use, self.city)

class Period(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()
    patient = models.ForeignKey(Patient, on_delete=models.PROTECT, related_name='Patient_Period', blank=True, null=True)
    practitioner = models.ForeignKey(Practitioner, on_delete=models.PROTECT, related_name='Practitioner_Period', blank=True, null=True)
    #contact = models.ForeignKey(Contact, on_delete=models.PROTECT, related_name='Contact_Telecom',blank=True, null=True)
    #name = models.ForeignKey(Name, on_delete=models.PROTECT, related_name='Contact_Telecom',blank=True, null=True)
    def __str__(self):
            return 'period starts : {} and ends {}'.format(self.start, self.end)