from django import forms
from .models import Account, ChargeItemDefinition, Practitioner, gender, ObservationDefinition, Slot , User, RecurrenceTemplate, Organization
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

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

class newcommentform(forms.Form):
    title = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Comment Title' }))
    body = forms.CharField(max_length=500, widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Comment in Detail' }))

class PatientRegistration(forms.Form):
    f_name = forms.CharField(label="First Name", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name', 'autocomplete':'off', 'onkeydown':"return /[a-z]/i.test(event.key)" }))
    m_name = forms.CharField(label="Middle Name", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Middle Name', 'autocomplete':"off", 'onkeydown':"return /[a-z]/i.test(event.key)" }))
    l_name = forms.CharField(label="Last Name", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last  Name', 'onkeydown':"return /[a-z]/i.test(event.key)" }))
    gender =  forms.ChoiceField(label="Gender", choices=gender, widget=forms.Select(attrs={'class': 'form-control', 'placeholder': 'Gender' }))
    birth_date = forms.DateField(label="DOB", required=False, widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'DOB YYYY-MM-DD' }))
    mobile = forms.IntegerField(label="Mobile", validators=[is_mobile],  widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Mobile',}))
    email = forms.EmailField(label="E Mail", required=False, widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'E Mail',}))
    photo = forms.ImageField(label='Add Image ', required=False,  widget=forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Photo',}))

class EncounterRegistration(forms.Form):
    practitioner = forms.ModelChoiceField(queryset=Practitioner.objects.all(), label = "Ref By", widget=forms.Select(attrs={'class': 'form-control selectpicker ', 'data-live-search':'true'}) )  
    test = forms.ModelMultipleChoiceField(queryset=ChargeItemDefinition.objects.all(), required=False,label = "Tests", widget=forms.SelectMultiple(attrs={'class': 'form-control chosen-select'}))
    account = forms.ModelChoiceField(queryset=Account.objects.all(), label = "Account", widget=forms.Select(attrs={'class': 'form-control selectpicker','data-live-search':'true'}))
    discount = forms.IntegerField(label="Discount", validators=[is_currency], required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Discount', 'onkeydown':"return /[0-9]/i.test(event.key)"}))
    paid = forms.IntegerField(label="Paid", validators=[is_currency], required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Paid', 'onkeydown':"return /[0-9]/i.test(event.key)"}))


class AppointmentRegistration (forms.Form): 
        description = forms.CharField(label="Description",  widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Description' }))
        start = forms.DateTimeField(label="start at", required=True, widget=forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Appointment Starts' }))
        end = forms.DateTimeField(label="end at", required=True, widget=forms.DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Appointment Ends' }))
        slot = forms.ModelChoiceField(queryset=Slot.objects.all(), label = "Slot", widget=forms.Select(attrs={'class': 'form-control selectpicker','data-live-search':'true'}))
        account = forms.ModelChoiceField(queryset=Account.objects.all(), label = "Account", widget=forms.Select(attrs={'class': 'form-control selectpicker','data-live-search':'true'}))
        participants = forms.ModelMultipleChoiceField(queryset=User.objects.all(), required=True,label = "Participants", widget=forms.SelectMultiple(attrs={'class': 'form-control chosen-select'}))
        recurrencetemplate = forms.ModelChoiceField(queryset=RecurrenceTemplate.objects.all(), label = "Recurrance ", widget=forms.Select(attrs={'class': 'form-control selectpicker','data-live-search':'true'}))
        organization = forms.ModelChoiceField(queryset=Organization.objects.all(), label = "TPA ", widget=forms.Select(attrs={'class': 'form-control selectpicker','data-live-search':'true'}))


class dummy (forms.Form):
    title = forms.CharField(label="Title", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title' }))
    price = forms.FloatField(label="Price", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Price' }))
    description = forms.CharField(label="Discription", widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Discription of Item' }))
    image = forms.ImageField(label='Add Image ', required=False)

