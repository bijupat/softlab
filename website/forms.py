from django import forms
from django.core.exceptions import ValidationError
#from django.utils.translation import gettext_lazy as _
from labsys.models import gender
from django.utils import timezone
from .models import FreeTestOfferAppointment
from django.core.validators import RegexValidator
from datetime import time

# this will convert DateInput's input type to date instead  of default 'text'
forms.DateInput.input_type="date"

# this will convert DateTimeInput's input type to datetime-local instead  of default 'text'
forms.DateTimeInput.input_type="datetime-local" 


# writing a validator that allow only mobile no ie 10 numberic Chars

def is_mobile(value):
    if len(str(value))!= 10:
        raise ValidationError(
            _('%(value)s is not an Valid mobile number'),
            params={'value': value},
        )
def is_currency(value):
    if value < 1 :
        raise ValidationError(
            _('%(value)s is not valid Amount'),
            params={'value': value},
        )


class FreeTestOfferBookingForm(forms.ModelForm):

    class Meta:
        model = FreeTestOfferAppointment
        fields = ['name', 'mobile', 'appointment_time']

    def clean_appointment_time(self):
        appointment_time = self.cleaned_data['appointment_time']
        if appointment_time < timezone.now():
            raise forms.ValidationError("Appointment time cannot be in the past.")
        if appointment_time.weekday() == 6:  # Sunday is 6
            raise forms.ValidationError("Appointments cannot be booked on Sundays.")
        if not time(8, 0) <= appointment_time.time() <= time(12, 0):
            raise forms.ValidationError("Appointment time must be 8 AM to 11:45 AM")
        if appointment_time.minute % 15 != 0:
            raise forms.ValidationError("Appointment time must be in 15-minute intervals like 9:00, 9:15, 9:30 10:00 etc.")
        slot_capacity = 1  # You can make this configurable elsewhere
        if not FreeTestOfferAppointment.slot_available(appointment_time, slot_capacity):
            raise forms.ValidationError("This time slot is fully booked.")
        return appointment_time
    def clean_name(self):
        name = self.cleaned_data['name'].strip()
        names = name.split()
        if len(names) < 2:
            raise forms.ValidationError("Name must be at least 2 word (first name and last name) long.")
        for n in names:
            if len(n) < 2:
                raise forms.ValidationError("first name and last name must be at least 2 ch long.")
            if not all(x.isalpha() or x.isspace() for x in n):
                raise forms.ValidationError("Name must contain only letters and spaces.")
        return name

    def clean_mobile(self):
        mobile = self.cleaned_data['mobile'].strip()
        validator = RegexValidator(r'^\d{10}$', 'Enter a valid mobile number with 10 digits.')
        validator(mobile)
        return mobile
    

class newcommentform(forms.Form):
    title = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Comment Title' }))
    body = forms.CharField(max_length=500, widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Comment in Detail' }))

class PatientRegistration(forms.Form):
    f_name = forms.CharField(label="First Name", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name*', 'autocomplete':'off', 'onkeydown':"return /[a-z]/i.test(event.key)" }))
    m_name = forms.CharField(label="Middle Name", required=False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Middle Name', 'autocomplete':"off", 'onkeydown':"return /[a-z]/i.test(event.key)" }))
    l_name = forms.CharField(label="Last Name", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last  Name', 'onkeydown':"return /[a-z]/i.test(event.key)" }))
    gender =  forms.ChoiceField(label="Gender", choices=gender, widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Gender' }))
    birth_date = forms.DateField(label="DOB", required=False, widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'DOB YYYY-MM-DD' }))
    mobile = forms.IntegerField(label="Mobile*", validators=[is_mobile],  widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Mobile*',}))
    email = forms.EmailField(label="E Mail", required=False, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'E Mail',}))
    visit_time  = forms.DateTimeField(label="Visit_time*", widget=forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Visit Time YYYY-MM-DD' }))
    tests = forms.CharField(label="Tests", required=False, max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Tests', }))
    address = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Address*', 'rows':'3',}))


"""
    class EncounterRegistration(forms.Form):
        practitioner = forms.ModelChoiceField(queryset=Practitioner.objects.all(), label = "Ref By", widget=forms.Select(attrs={'class': 'form-control selectpicker ', 'data-live-search':'true'}) )  
        test = forms.ModelMultipleChoiceField(queryset=ChargeItemDefinition.objects.all(), required=False,label = "Tests", widget=forms.SelectMultiple(attrs={'class': 'form-control chosen-select'}))
        account = forms.ModelChoiceField(queryset=Account.objects.all(), label = "Account", widget=forms.Select(attrs={'class': 'form-control selectpicker','data-live-search':'true'}))
        discount = forms.IntegerField(label="Discount", validators=[is_currency], required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Discount', 'onkeydown':"return /[0-9]/i.test(event.key)"}))
        paid = forms.IntegerField(label="Paid", validators=[is_currency], required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Paid', 'onkeydown':"return /[0-9]/i.test(event.key)"}))


    class AppointmentRegistration (forms.Form): 
            description = forms.CharField(label="Description",  widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description', 'rows': 5, 'style':"width:100%;" }))
            start = forms.DateTimeField(label="Start at", required=True, widget=forms.DateTimeInput(attrs={'class': 'form-control' }))
            end = forms.DateTimeField(label="End at", required=True, widget=forms.DateTimeInput(attrs={'class': 'form-control' }))
            slot = forms.ModelChoiceField(queryset=Slot.objects.all(), required=False, label = "Slot", widget=forms.Select(attrs={'class': 'form-control selectpicker','data-live-search':'true'}))
            account = forms.ModelChoiceField(queryset=Account.objects.all(), label = "Account", widget=forms.Select(attrs={'class': 'form-control selectpicker','data-live-search':'true'}))
            participants = forms.ModelMultipleChoiceField(queryset=User.objects.all(), required=True,label = "Participants", widget=forms.SelectMultiple(attrs={'class': 'form-control selectpicker chosen-select', 'data-live-search':'true'}))
            recurrencetemplate = forms.ModelChoiceField(queryset=RecurrenceTemplate.objects.all(), required=False, label = "Recurrance ", widget=forms.Select(attrs={'class': 'form-control selectpicker' ,'data-live-search':'true'}))
            organization = forms.ModelChoiceField(queryset=Organization.objects.all(), label = "TPA ", widget=forms.Select(attrs={'class': 'form-control selectpicker ','data-live-search':'true'}))
            tests = forms.ModelMultipleChoiceField(queryset=ChargeItemDefinition.objects.all(), required=False,label = "Tests", widget=forms.SelectMultiple(attrs={'class': 'form-control selectpicker chosen-select', 'data-live-search':'true'}))
            patientinstruction = forms.CharField(label="Patient Instruction",  widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Patient Instruction', 'rows': 5, 'style':"width:100%;" }))
            priority = forms.BooleanField(label="Is High Priority",required=False, widget=forms.CheckboxInput(attrs={'class': 'form-control',  }))

    class dummy (forms.Form):
        title = forms.CharField(label="Title", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title' }))
        price = forms.FloatField(label="Price", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Price' }))
        description = forms.CharField(label="Discription", widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Discription of Item' }))
        image = forms.ImageField(label='Add Image ', required=False)

"""
