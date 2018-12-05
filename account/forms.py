from django import forms
from django.forms import widgets
from django.forms import fields

class LoginForm(forms.Form):
    username = forms.CharField(widget=widgets.TextInput(attrs={"class":"form-control","placeholder": "用户名"}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder": "密码"}))