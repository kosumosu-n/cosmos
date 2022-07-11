from django import forms
from .models import Notes


class Notes(forms.ModelForm):
    class Meta:
        model = Notes
        exclude = ['tag','created']