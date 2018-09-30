from django import forms
from captcha.fields import CaptchaField
import datetime

class RegisterForm(forms.Form):
    email = forms.EmailField(required=True,error_messages={'invalid':'邮箱格式不正确'})
    password = forms.CharField(required=True,min_length=6,error_messages={'min_length':'密码长度不够'})
    captcha = CaptchaField(required=True,error_messages={'invalid':'验证码错误'})

class LoginForm(forms.Form):
    email = forms.EmailField(required=True,error_messages={'invalid':'邮箱格式不正确'})
    password = forms.CharField(required=True,min_length=6,error_messages={'min_length':'密码长度不够'})

class ForgetForm(forms.Form):
    email = forms.EmailField(required=True,error_messages={'invalid':'邮箱格式不正确'})

class ResetForm(forms.Form):
    password = forms.CharField(required=True,min_length=6,error_messages={'min_length':'密码长度小于六位'})
    again = forms.CharField(required=True,min_length=6,error_messages={'min_length':'密码长度小于六位'})
class InfoForm(forms.Form):
    name = forms.CharField(required=True,error_messages={'invalid':'名称不能为空'})
    amount = forms.FloatField(required=True,error_messages={'invalid':'学费不能为空'})
    days = forms.IntegerField(required=True,error_messages={'invalid':'学时不能为空'})
    assurance = forms.CharField(required=True,max_length=200,error_messages={'max_length':'承诺过多,太假'})
    remark = forms.CharField(required=True,max_length=200,error_messages={'max_length':'备注过长,假'})