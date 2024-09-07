# projects/forms.py
from django import forms
from .models import Inquiry

class ContactForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = ['full_name', 'email', 'subject', 'message']
