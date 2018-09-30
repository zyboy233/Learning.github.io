from django import forms
from  captcha.fields import CaptchaField
class RegistForm(forms.Form):
    email = forms.EmailField(required=True,error_messages={'invalid':'邮箱格式不正确'})
    password = forms.CharField(required=True,min_length=6,error_messages={'min_length':'密码少于6位'})
    captcha = CaptchaField(required=True,error_messages={'invalid':'验证码错误'})

class LoginForm(forms.Form):
    email = forms.EmailField(required=True, error_messages={'invalid': '邮箱格式不正确'})
    password = forms.CharField(required=True, min_length=6, error_messages={'min_length': '密码少于6位'})
class EmailForm(forms.Form):
    email = forms.EmailField(required=True, error_messages={'invalid': '邮箱格式不正确'})