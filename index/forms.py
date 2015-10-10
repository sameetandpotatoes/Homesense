from django import forms
from django.contrib.auth.forms import AuthenticationForm
class LoginForm(AuthenticationForm):
    username = forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={
            'title': 'Username',
            'id': 'id_username',
            'name': 'username'
        }))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
             'title':'Password',
             'id':'id_password',
             'name':'password'
        }))

class GroupForm(forms.Form):
    name= forms.CharField(max_length = 100)

class SensorForm(forms.Form):
    name= forms.CharField(max_length = 100)
