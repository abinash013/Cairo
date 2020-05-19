from django import forms
from .models import details

class signinform(forms.ModelForm):
    class Meta:
        model = details
        fields = ["name", "password", "address", "phone", "email"]
        widgets = {
        'password': forms.PasswordInput(),
    }
