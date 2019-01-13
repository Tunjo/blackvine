from django import forms
from django.contrib.auth.forms import UserCreationForm



class CustomerForm(UserCreationForm):

    user_name = forms.CharField(required=True, widget=forms.TextInput())
    first_name = forms.CharField(required=True, widget=forms.TextInput())
    last_name = forms.CharField(required=True, widget=forms.TextInput())
    email = forms.EmailField(required=True, widget=forms.TextInput())
    password_one = forms.CharField(required=True,
                                   widget=forms.TextInput(attrs={'type': 'password'}))
    password_two = forms.CharField(required=True,
                                   widget=forms.TextInput(attrs={'type': 'password'}))

