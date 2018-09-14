from django import forms

class RegisterForm(forms.Form):
    eamil = forms.EmailField(required=True)
    passsword = forms.CharField(required=True,min_length=6)