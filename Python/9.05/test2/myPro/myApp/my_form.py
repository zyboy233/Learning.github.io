from django import forms

class AddForm(forms.Form):
    inpt1 = forms.CharField(label='标签1')
    inpt2 = forms.CharField(label='标签2')