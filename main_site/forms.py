from django import forms
from .models import Client

class MainSiteClientSignupForm(forms.ModelForm):

    class meta():
        model = Client
        fields = [
            'forename',
            'surname',
            'gender',
            'phone_number',
            'email',
            'password',
        ]