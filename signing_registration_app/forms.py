from django.utils.translation import gettext_lazy as _
from django.forms import DateInput
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser
from django import forms

class RegistrationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'photo', 'birthday')
        widgets = {
            'birthday': DateInput(attrs={'type': 'date'})
        }

class CustomAuthenticationForm(AuthenticationForm):
   class Meta:
        model = CustomUser
        fields = ('email', 'password')
        widgets = {
            'email': forms.EmailInput(attrs={'autofocus': True}),
        }
        labels = {
            'email': _('Email'),
        }
        error_messages = {
            'email': {
                'required': _('Please enter your email'),
                'invalid': _('Please enter a valid email address'),
            },
            'password': {
                'required': _('Please enter your password'),
            },
        }