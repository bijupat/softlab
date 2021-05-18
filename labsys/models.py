from django_pg import models

class name(models.CompositeField):
    use = models.CharField(max_length=7, blank=True, null=True5)
    text = models.CharField(max_length=75)
    family = models.CharField(max_length=75, blank=True, null=True)
    given = models.CharField(max_length=75, blank=True, null=True)
    prefix = models.CharField(max_length=75, blank=True, null=True)
    suffix = models.CharField(max_length=75, blank=True, null=True)
    period = period()

    def __str__(self):
            return 'name : {}'.format(self.text)

class period(models.CompositeField):
    start = models.DateTimeField()
    end = models.DateTimeField()

    def __str__(self):
            return 'period starts : {} and ends {}'.format(self.start, self.end)

class telecom(models.CompositeField):
    system = models.CharField(max_length=75, blank=True, null=True)
    value = models.CharField(max_length=75, blank=True, null=True)
    use = models.CharField(max_length=75, blank=True, null=True)
    rank = models.IntegerField(blank=True, null=True)

    def __str__(self):
            return 'telecom  : {} is  {}'.format(self.system, self.value)

class contact(models.CompositeField):
    relationship = models.CharField(max_length=75, blank=True, null=True)
    name = name()
    telecom = telecom()
    address =  address()
    gender = models.CharField(max_length=75, blank=True, null=True)
    period = period()
    def __str__(self):
            return 'contact  : {} is  {}'.format(self.name, self.relationship)

class qualification(models.CompositeField):
    identifier = models.CharField(max_length=75, blank=True, null=True, related_name="regiNo")
    degree = models.CharField(max_length=75, blank=True, null=True)
    period = period()
    issuer = models.CharField(max_length=75, blank=True, null=True) # can be foreign key to organisation table
    
    def __str__(self):
            return 'degree  : {} having reg no  {} issued by {}'.format(self.degree, self.identifier, self.issuer)
    

class note(models.CompositeField):
    author = models.ForeignKey(Practitioner, on_delete=models.PROTECT, related_name='Note_by')
    time = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=500, blank=True, null=True)
    
    def __str__(self):
            return 'Note by   : {} at : {}'.format(self.author, self.time)

class address(models.CompositeField):
    use = models.CharField(max_length=75, blank=True, null=True)
    text = models.CharField(max_length=250, blank=True, null=True)
    line = models.CharField(max_length=250, blank=True, null=True)
    city = models.CharField(max_length=75, blank=True, null=True)
    district = models.CharField(max_length=75, blank=True, null=True)
    state = models.CharField(max_length=250, blank=True, null=True)
    postalCode = models.CharField(max_length=250, blank=True, null=True)
    country = models.CharField(max_length=250, blank=True, null=True)
    period = period()

    def __str__(self):
            return 'address : {} at : {}'.format(self.use, self.city)

class Patient(models.Model):
    identifier = models.CharField(max_length=75, blank=True, null=True, related_name = "Unique Health ID")
    active = models.BooleanField(blank=True, null=True, default=True)
    name = name()
    telecom = telecom()
    gender = models.CharField(max_lenth=25)
    birthDate = models.DateField(blank=True, null=True)
    deceasedBoolean = models.BooleanField(blank=True, null=True, default=False)
    address = address()
    photo = models.ImageField(blank=true, null=true)
    concact = concact()
    communication = models.CharField(max_length=75, blank=True, null=True, related_name = "Communication Laung")
    generalPractitioner = models.ForeignKey(Practitioner, on_delete=models.PROTECT, related_name='Ref_by_GP')
    

    def __str__(self):
        return 'Person name : {}'.format(self.name)

class Practitioner(models.Model):
    identifier = models.CharField(max_length=75, blank=True, null=True, related_name = "Regi_No_of_Practitioner")
    active = models.BooleanField(blank=True, null=True, default=True)
    name = name()
    telecom = telecom()
    gender = models.CharField(max_lenth=25)
    birthDate = models.DateField(blank=True, null=True)
    deceasedBoolean = models.BooleanField(blank=True, null=True, default=False)
    address = address()
    photo = models.ImageField(blank=true, null=true)
    qualification = qualification()
    communication = communication()

    def __str__(self):
        return 'Practitioner name : {}'.format(self.name)



    

    
