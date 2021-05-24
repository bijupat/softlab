from django.db import models


class period(models.Model):
    start = models.DateTimeField()
    end = models.DateTimeField()

    def __str__(self):
            return 'period starts : {} and ends {}'.format(self.start, self.end)

class name(models.Model):
    use = models.CharField(max_length=7, blank=True, null=True)
    text = models.CharField(max_length=75)
    family = models.CharField(max_length=75, blank=True, null=True)
    given = models.CharField(max_length=75, blank=True, null=True)
    prefix = models.CharField(max_length=75, blank=True, null=True)
    suffix = models.CharField(max_length=75, blank=True, null=True)
    period = models.OneToOneField(period, on_delete=models.PROTECT)

    def __str__(self):
            return 'name : {}'.format(self.text)


class telecom(models.Model):
    system = models.CharField(max_length=75, blank=True, null=True)
    value = models.CharField(max_length=75, blank=True, null=True)
    use = models.CharField(max_length=75, blank=True, null=True)
    rank = models.IntegerField(blank=True, null=True)

    def __str__(self):
            return 'telecom  : {} is  {}'.format(self.system, self.value)

class address(models.Model):
    use = models.CharField(max_length=75, blank=True, null=True)
    text = models.CharField(max_length=250, blank=True, null=True)
    line = models.CharField(max_length=250, blank=True, null=True)
    city = models.CharField(max_length=75, blank=True, null=True)
    district = models.CharField(max_length=75, blank=True, null=True)
    state = models.CharField(max_length=250, blank=True, null=True)
    postalCode = models.CharField(max_length=250, blank=True, null=True)
    country = models.CharField(max_length=250, blank=True, null=True)
    period = models.OneToOneField(period, on_delete=models.PROTECT)

    def __str__(self):
            return 'address : {} at : {}'.format(self.use, self.city)

class contact(models.Model):
    relationship = models.CharField(max_length=75, blank=True, null=True)
    name = name()
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
    name = name()
    telecom = telecom()
    gender = models.CharField(max_length=75)
    birthDate = models.DateField(blank=True, null=True)
    deceasedBoolean = models.BooleanField(blank=True, null=True, default=False)
    address = address()
    photo = models.ImageField()
    concact = contact()
    communication = models.CharField(max_length=75, blank=True, null=True)
    generalPractitioner = models.ForeignKey(Practitioner, on_delete=models.PROTECT, related_name='Ref_by_GP')
    

    def __str__(self):
        return 'Person name : {}'.format(self.name)  
