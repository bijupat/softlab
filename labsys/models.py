from django.db import models


class period(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()

    def __str__(self):
            return 'period starts : {} and ends {}'.format(self.start, self.end)

class name(models.Model):
    # // usual | official | temp | nickname | anonymous | old | maiden
    use = models.CharField(max_length=7, blank=True, null=True)
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
    period = models.OneToOneField(period, on_delete=models.PROTECT, blank=True)

    def __str__(self):
            return 'name : {}'.format(self.text)


class telecom(models.Model):
    # phone | fax | email | pager | url | sms | other
    system = models.CharField(max_length=75, blank=True, null=True)
    # The actual contact point details
    value = models.CharField(max_length=75, blank=True, null=True)
    # // home | work | temp | old | mobile - purpose of this contact point
    use = models.CharField(max_length=75, blank=True, null=True)
    # // Specify preferred order of use (1 = highest)
    rank = models.IntegerField(blank=True, null=True)

    def __str__(self):
            return 'telecom  : {} is  {}'.format(self.system, self.value)

class address(models.Model):
    # // home | work | temp | old | billing - purpose of this address
    use = models.CharField(max_length=75, blank=True, null=True)
    # // Text representation of the address
    text = models.CharField(max_length=250, blank=True, null=True)
    # // Street name, number, direction & P.O. Box etc.
    line = models.CharField(max_length=250, blank=True, null=True)
    # // Name of city, town etc.
    city = models.CharField(max_length=75, blank=True, null=True)
    district = models.CharField(max_length=75, blank=True, null=True)
    state = models.CharField(max_length=250, blank=True, null=True)
    postalCode = models.CharField(max_length=250, blank=True, null=True)
    country = models.CharField(max_length=250, blank=True, null=True)
    # Time period when name was/is in use
    period = models.OneToOneField(period, on_delete=models.PROTECT)

    def __str__(self):
            return 'address : {} at : {}'.format(self.use, self.city)
# // A contact party (e.g. guardian, partner, friend) for the patient##
class contact(models.Model):
    # // The kind of relationship
    relationship = models.CharField(max_length=75, blank=True, null=True)
    # A name associated with the contact person
    name = models.OneToOneField(name, on_delete=models.PROTECT)

    telecom = telecom()
    address =  address()
    gender = models.CharField(max_length=75, blank=True, null=True)
    period = period()
    def __str__(self):
            return 'contact  : {} is  {}'.format(self.name, self.relationship)

class qualification(models.Model):
    identifier = models.CharField(max_length=75, blank=True, null=True)
    degree = models.CharField(max_length=75, blank=True, null=True)
    period = period()
    issuer = models.CharField(max_length=75, blank=True, null=True) # can be foreign key to organisation table
    
    def __str__(self):
            return 'degree  : {} having reg no  {} issued by {}'.format(self.degree, self.identifier, self.issuer)
    







class Practitioner(models.Model):
    identifier = models.CharField(max_length=75, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True, default=True)
    name = name()
    telecom = telecom()
    gender = models.CharField(max_length=75)
    birthDate = models.DateField(blank=True, null=True)
    deceasedBoolean = models.BooleanField(blank=True, null=True, default=False)
    address = address()
    photo = models.ImageField()
    qualification = qualification()
    #communication = communication()

    def __str__(self):
        return 'Practitioner name : {}'.format(self.name)



class note(models.Model):
    author = models.ForeignKey(Practitioner, on_delete=models.PROTECT, related_name='Note_by')
    time = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=500, blank=True, null=True)
    
    def __str__(self):
            return 'Note by   : {} at : {}'.format(self.author, self.time)

class Patient(models.Model):
    identifier = models.CharField(max_length=75, blank=True, null=True)
    active = models.BooleanField(blank=True, null=True, default=True)
    name = models.ForeignKey(name, on_delete=models.PROTECT, related_name='Patient_Name')
    birthDate = models.DateField(blank=True, null=True)
    deceasedBoolean = models.BooleanField(blank=True, null=True, default=False)
    address = models.ForeignKey(address, on_delete=models.PROTECT, related_name='Patient_Address')
    photo = models.ImageField()
    concact = models.ForeignKey(contact, on_delete=models.PROTECT, related_name='Patient_Contact')
    communication = 0
     
    generalPractitioner = models.ForeignKey(Practitioner, on_delete=models.PROTECT, related_name='Ref_by_GP')
    

    def __str__(self):
        return 'Person name : {}'.format(self.name)  
