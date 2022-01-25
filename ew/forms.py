from django import forms
from .models import Examples, Words

class Wuf(forms.ModelForm):

    class Meta:
        model = Words
        exclude = ['created', 'browsed',]

class Exaf(forms.ModelForm):

    class Meta:
        model = Examples
        exclude = ['created']

class Exuf(forms.ModelForm):

    class Meta:
        model = Examples
        exclude = ['created']


class AddForm(forms.Form):
    spell = forms.CharField(label='単語', widget=forms.Textarea)
    ts = forms.CharField(label='訳', required=False, widget=forms.Textarea)
    pt = forms.CharField(label='過去形', required=False, widget=forms.Textarea)
    pp = forms.CharField(label='過去分詞形', required=False, widget=forms.Textarea)
    prp = forms.CharField(label='現在分詞形', required=False, widget=forms.Textarea)
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.label_suffix = " "