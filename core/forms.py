from django import forms
from phonenumber_field.formfields import PhoneNumberField


class ContactForm(forms.Form):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    phone = PhoneNumberField(required=True)
    company = forms.CharField(required=True)
    message = forms.CharField(required=True, widget=forms.Textarea)
    
