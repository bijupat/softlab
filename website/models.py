from django.db import models
from labsys.models import appointment_status, User, gender
# import hashlib
import uuid
from django.utils import timezone
from django.contrib.postgres.indexes import GinIndex
import random
import string
# from django.core.exceptions import ValidationError

class FreeTestOfferAppointment(models.Model):
    name = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    sms_verified = models.BooleanField(default=False)
    unique_code = models.CharField(max_length=12, unique=True, blank=True)
    appointment_time = models.DateTimeField()
    slot_capacity = models.IntegerField(default=1)

    def save(self, *args, **kwargs):
        if not self.unique_code:
            self.unique_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=12))
        super().save(*args, **kwargs)

    @classmethod
    def slot_available(cls, appointment_time, slot_capacity):
        start = appointment_time.replace(minute=(appointment_time.minute // 15) * 15, second=0, microsecond=0)
        end = start + timezone.timedelta(minutes=15)
        count = cls.objects.filter(appointment_time__gte=start, appointment_time__lt=end).count()
        return count < slot_capacity

    # def clean(self):
    #     if not self.appointment_time:
    #         pass
    #     if self.appointment_time.minute % 15 != 0:
    #         raise ValidationError("Appointment time must be in 15-minute intervals.")
    #     if not self.slot_available(self.appointment_time, self.slot_capacity):
    #         raise ValidationError("This appointment slot is full.")
   
class WebsiteVisitor(models.Model):
    ip_address = models.GenericIPAddressField()
    user_agent = models.TextField(blank=True, null=True)
    visit_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Visitor {self.ip_address} at {self.visit_time}"
    
    
class Advertisement(models.Model):
    name = models.CharField(max_length=255)
    platform = models.CharField(max_length=100)
    notes = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [models.Index(fields=["is_active"]), models.Index(fields=["platform"])]

    def __str__(self):
        return f"{self.name} ({self.platform})"


class AdLink(models.Model):
    advertisement = models.ForeignKey(Advertisement, on_delete=models.CASCADE, related_name="links")
    short_code = models.CharField(max_length=20, unique=True, editable=False)
    target_url = models.URLField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [models.Index(fields=["short_code"]), models.Index(fields=["is_active"])]

    def save(self, *args, **kwargs):
        if not self.short_code:
            self.short_code = uuid.uuid4().hex[:10]
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.short_code} → {self.target_url}"


class VisitorFingerprint(models.Model):
    hashed_ip = models.CharField(max_length=64, db_index=True)
    user_agent = models.TextField()
    accept_headers = models.TextField()
    fingerprint_hash = models.CharField(max_length=64, unique=True, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [GinIndex(fields=["fingerprint_hash"])]

    def __str__(self):
        return self.fingerprint_hash


class AdVisit(models.Model):
    ad_link = models.ForeignKey(AdLink, on_delete=models.CASCADE, related_name="visits")
    visitor_fingerprint = models.ForeignKey(VisitorFingerprint, on_delete=models.SET_NULL, null=True, blank=True)
    hashed_ip = models.CharField(max_length=64, db_index=True)
    user_agent = models.TextField()
    browser = models.CharField(max_length=100)
    os = models.CharField(max_length=100)
    device_type = models.CharField(max_length=50)  # mobile/desktop/tablet
    referrer = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(default=timezone.now)
    geo_info = models.JSONField(blank=True, null=True)

    class Meta:
        indexes = [
            models.Index(fields=["ad_link"]),
            models.Index(fields=["timestamp"]),
            models.Index(fields=["hashed_ip"]),
        ]

    def __str__(self):
        return f"Visit {self.ad_link.short_code} at {self.timestamp.isoformat()}"
    
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