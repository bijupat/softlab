from django import forms

CATEGORY_CHOICES = (
        
    ('APPARELS', 'APPARELS'),
    ('CONSUMER ELECTRONICS', 'CONSUMER ELECTRONICS'),
    ('FOOTWEAR', 'FOOTWEAR'),
    ('FOOD, HEALTH', 'FOOD, HEALTH'),
    ('JEWELLERY', 'JEWELLERY'),
    ('BOOKS', 'BOOKS'),
    ('MOBILE PHONES', 'MOBILE PHONES'),
    ('FASHION ACCESSORIES', 'FASHION ACCESSORIES'),
    ('HOME DECOR ITEMS', 'HOME DECOR ITEMS'),
    ('KITCHEN WARE', 'KITCHEN WARE'),
    ('TOYS AND GAMES', 'TOYS AND GAMES'),
    ('COMPUTER', 'COMPUTER'),
    ('Others', 'Others')
)

LABEL_CHOICES = (
    ('New', 'New'),
    ('Used', 'Used'),
    ('Refurbished', 'Refurbished')
)

class newcommentform(forms.Form):
    title = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Comment Title' }))
    body = forms.CharField(max_length=500, widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Comment in Detail' }))


class PatientRegistration(forms.Form):
    title = forms.CharField(label="Title", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Title' }))
    price = forms.FloatField(label="Price", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Price' }))
    category = forms.ChoiceField(label="Category", choices=CATEGORY_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    label = forms.ChoiceField(label="Condition", choices=LABEL_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    description = forms.CharField(label="Discription", widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Discription of Item' }))
    image = forms.ImageField(label='Add Image ', required=False)

class selectcategory(forms.Form):
    category = forms.ChoiceField(label="Category", choices=CATEGORY_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
