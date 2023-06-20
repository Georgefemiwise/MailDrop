from django import forms

class EmailForm(forms.Form):
     subject = forms.CharField(min_length=10)
     message =forms.CharField(max_length=100)

