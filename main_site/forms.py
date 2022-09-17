from django import forms
from django.contrib.auth import password_validation
from .models import Client

class MainSiteClientSignupForm(forms.ModelForm):

    password_conf = forms.CharField(max_length=24)

    class Meta:
        model = Client
        fields = [
            'forename',
            'surname',
            'gender',
            'phone_number',
            'email',
            'password',
        ]