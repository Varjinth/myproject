from django import forms

class MyForm(forms.Form):
    url = forms.CharField(max_length=100)