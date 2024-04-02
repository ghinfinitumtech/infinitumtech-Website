
# forms.py
from django import forms
from .models import CareerApplication
from django import forms
from myApp.models import *

class CareerApplicationForm(forms.ModelForm):
   
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    ]

    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.Select(attrs={'class': 'form-control'}))
    date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}, format='%d-%m-%Y'))

    class Meta:
        model = CareerApplication
        fields = ['name', 'email', 'resume', 'phone', 'address', 'date', 'gender']


class Contact_Form(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ['name', 'email',  'subject', 'phone','message']
