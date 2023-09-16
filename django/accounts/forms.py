from django.contrib.auth.forms import UserCreationForm
from . models import UserTable
from django.db import models
from django import forms

class UserForm(UserCreationForm):
    class Meta:
        model = UserTable
        fields = ['username','email','password1','password2']
        
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2','placeholder':'Enter Username'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2','placeholder':'Enter email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control my-2','placeholder':'Enter password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control my-2','placeholder':'Confirm password'}))