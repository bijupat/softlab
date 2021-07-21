from django import forms
from .models import Account, Practitioner, gender, ObservationDefinition


class newcommentform(forms.Form):
    title = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Comment Title' }))
    body = forms.CharField(max_length=500, widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Comment in Detail' }))

class PatientRegistration(forms.Form):
    f_name = forms.CharField(label="First Name", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'id':'exampleFormControlInput1', 'placeholder': 'First Name' }))
    m_name = forms.CharField(label="Middle Name", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'id':'exampleFormControlInput1', 'placeholder': 'Middle Name' }))
    l_name = forms.CharField(label="Last Name", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'id':'exampleFormControlInput1', 'placeholder': 'Last  Name' }))
    gender =  forms.ChoiceField(label="Gender", choices=gender, widget=forms.TextInput(attrs={'class': 'form-control', 'id':'exampleFormControlInput1', 'placeholder': 'Gender' }))
    birth_date = forms.DateField(label="DOB", required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'id':'exampleFormControlInput1', 'placeholder': 'DOB YYYY-MM-DD' }))
    mobile = forms.IntegerField(label="Mobile", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mobile', 'id':'exampleFormControlInput1'}))
    photo = forms.ImageField(label='Add Image ', required=False)
    practitioner = forms.ModelChoiceField(queryset=Practitioner.objects.all(), label = "Ref By")  
    test = forms.ModelMultipleChoiceField(queryset=ObservationDefinition.objects.all(), label = "Tests")
    account = forms.ModelChoiceField(queryset=Account.objects.all(), label = "Account")
    discount = forms.IntegerField(label="Discount", required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Discount', 'id':'exampleFormControlInput1'}))
    paid = forms.IntegerField(label="Paid", required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Paid', 'id':'exampleFormControlInput1'}))

class dummy (forms.Form):
    title = forms.CharField(label="Title", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title' }))
    price = forms.FloatField(label="Price", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Price' }))
    description = forms.CharField(label="Discription", widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Discription of Item' }))
    image = forms.ImageField(label='Add Image ', required=False)

