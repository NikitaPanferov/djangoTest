from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms import ModelForm

from .models import *


class AddPostForm(ModelForm):
    class Meta:
        model = Posts
        fields = '__all__'


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='', required=True, widget=forms.TextInput(attrs={
        'class': 'form-control my-1',
        'placeholder': 'Логин',
        'autofocus': 'True'}))
    password1 = forms.CharField(label='', required=True, widget=forms.PasswordInput(attrs={
        'class': 'form-control my-1',
        'placeholder': 'Пароль'
    }))
    password2 = forms.CharField(label='', required=True, widget=forms.PasswordInput(attrs={
        'class': 'form-control my-1',
        'placeholder': 'Повторите пароль',
    }))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2')


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='', required=True, widget=forms.TextInput(attrs={
        'class': 'form-control upper-input',
        'placeholder': 'Логин',
        'autofocus': 'True'}))
    password = forms.CharField(label='', required=True, widget=forms.PasswordInput(attrs={
        'class': 'form-control bottom-input',
        'placeholder': 'Пароль'
    }))
