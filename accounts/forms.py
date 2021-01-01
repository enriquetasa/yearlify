from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import User

class RegisterForm(UserCreationForm):

    class Meta:
        model = User
        fields = [
            'name', 
            'email', 
            'password1',
            'password2',
            ]
        labels = {
            'name': 'What is your name?',
            'email': 'What email should we use to contact you (only once a year)?',
            'password1': 'Password',
            'password2': 'Confirm Password'
        }
