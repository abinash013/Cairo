from django import forms
from .models import details

class signinform(forms.ModelForm):
    class Meta:
        model = details
        fields = ["name", "password", "address", "phone", "email"]
        widgets = {
        'password': forms.PasswordInput(),
    }

class loginform(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget = forms.PasswordInput())
