from django import forms

class Note(forms.Form):
    text = forms.CharField(widget=forms.Textarea, label='', max_length=500)