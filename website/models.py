from django.db import models
from labsys.models import appointment_status, User, gender


    
class Patient(models.Model):
    f_name = models.CharField(max_length=75)
    m_name = models.CharField(max_length=75, blank=True, null=True)
    l_name = models.CharField(max_length=75, blank=True, null=True)
    mobile = models.CharField(max_length=10)
    email = models.EmailField(blank=True, null=True)
    gender = models.CharField(max_length=20, choices=gender,blank=True, null=True)
    birthDate = models.DateField(blank=True, null=True)
    address = models.CharField(max_length=250)

    def __str__(self):
        return 'Patient : {}'.format(self.f_name)

# Create your models here.
class Appointment(models.Model):
    #  proposed | pending | booked | arrived | fulfilled | cancelled | noshow | entered-in-error | checked-in | waitlist|
    status = models.CharField(max_length=75, blank=True, null=True, default='B', choices=appointment_status)
    cancelationreason = models.CharField(max_length=75, blank=True, null=True)
    # Used to make informed decisions if needing to re-prioritize
    priority = models.BooleanField(blank=True, null=True, default=False)
    # Shown on a subject line in a meeting request, or appointment list
    description = models.CharField(max_length=75, blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True)
     # The date that this appointment was initially created
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    # the user who creatd appointment
    updated_by = models.ForeignKey(User, on_delete=models.PROTECT, related_name='appointment_updated', blank=True, null=True)
    # When the appointment was cancelled
    subject = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='appointments_booked', null=True, blank=True)
    #users needed during appointment
    tests = models.CharField(max_length=200, blank=True, null=True)
    
    def __str__(self):
        return 'Appointment for : {} at : {}'.format(self.subject, self.time)
