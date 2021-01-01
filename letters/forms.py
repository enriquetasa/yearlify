from django.forms import ModelForm
from django import forms

from .models import (
    Letter
)

class LetterForm(ModelForm):

    content = forms.CharField(widget=forms.Textarea())

    class Meta:
        model = Letter
        fields = [
            'content'
            ]
        labels = {
            'content' : ""
            }
