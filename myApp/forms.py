
# forms.py
from django import forms
from .models import CareerApplication
from django import forms
from myApp.models import *

from django import forms
from .models import CareerApplication

class CareerApplicationForm(forms.ModelForm):
    class Meta:
        model = CareerApplication
        fields = ['name', 'email', 'resume', 'phone', 'address', 'date', 'gender']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name', 'required': True}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email', 'required': True}),
            'gender': forms.Select(attrs={'class': 'form-control', 'required': True}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),
            'resume': forms.FileInput(attrs={'class': 'form-control-file', 'accept': 'application/pdf,application/msword,application/vnd.openxmlformats-officedocument.wordprocessingml.document', 'required': True}),
        }

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'phone', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your name here'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Your email here'}),
            'subject': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Your subject here'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Your phone here'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Tell us a few words'}),
        }
