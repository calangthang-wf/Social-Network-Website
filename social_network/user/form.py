from operator import attrgetter
import re
from tkinter import Widget
from django import forms
from django.contrib.auth.models import User




class RegistrationForm(forms.ModelForm):
    username = forms.CharField(
        max_length=30,
        widget=forms.widgets.Textarea(
            attrs={
                "class": "username"
            }
        )
    )
    
    email = forms.EmailField(
        widge= forms.EmailField(
            attrs = {
                "class": "email"
            }
        )
    )
    
    
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs= {
                "class": "password"
            }
        )
    )
    
    repassword = forms.CharField(
        widget=forms.PasswordInput(
            attrs= {
                "class": "repassword"
            }
        )
    )
    
    def clean_password(self):  # compare passwords
        if 'password' in self.cleaned_data:
            password = self.cleaned_data['password']
            repassword = self.cleaned_data['repassword']
            if password == repassword and password:  #avoid users using space
                return repassword
            raise forms.ValidationError("PassWord Invalid!")
        
    def clean_username(self):
        username = self.cleaned_data['username']
        if not re.search(r'^\w$', username):  # check speacial characters
            raise forms.ValidationError('Username has special characters!')
        try:     # check username
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError("Username has already existed!")