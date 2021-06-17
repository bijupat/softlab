from django import forms
from .models import gender, ObservationDefinition


class newcommentform(forms.Form):
    title = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Comment Title' }))
    body = forms.CharField(max_length=500, widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Comment in Detail' }))

class PatientRegistration:
    f_name = forms.CharField(label="First Name", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name' }))
    m_name = forms.CharField(label="Middle Name", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Middle Name' }))
    l_name = forms.CharField(label="Last Name", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last  Name' }))
    gender =  forms.ChoiceField(label="Gender", choices=gender, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Gender' }))
    birth_date = forms.DateField(label="DOB", required=False, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'DOB' }))
    mobile = forms.IntegerField(label="Mobile", widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Mobile' }))
    photo = forms.ImageField(label='Add Image ', required=False)    
    test = forms.ModelMultipleChoiceField(queryset=ObservationDefinition.objects.all())

class dummy (forms.Form):
    title = forms.CharField(label="Title", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title' }))
    price = forms.FloatField(label="Price", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Price' }))
    description = forms.CharField(label="Discription", widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Discription of Item' }))
    image = forms.ImageField(label='Add Image ', required=False)

