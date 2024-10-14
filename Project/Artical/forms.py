from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm

class SignUpForm(UserCreationForm):
   
    username = forms.CharField(
    help_text='',
    label='Логин'
   )
    password1 = forms.CharField(
    help_text='',
    label='Пароль:'
   )
    password2 = forms.CharField(
    help_text='',
    label='Пароль:'
   )

    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email', 'password1', 'password2', )

class UserLoginForm(AuthenticationForm):
    username = forms.CharField(
    help_text='',
    label='Логин'
    )
    password = forms.CharField(
    help_text='',
    label='Пароль:'
   )
    class Meta:
        model = User
        fields = ('username','password')

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)