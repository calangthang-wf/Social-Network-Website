
from operator import attrgetter
from tkinter import Widget
from django import forms
from .models import Post_content

class PostForm(forms.ModelForm):
    content = forms.CharField(
        required=True,
        widget=forms.widgets.Textarea(
            attrs={
                "placeholder": "write something...",
                "rows": "2",
            }
        )
    )
    image = forms.ImageField(
        required=False,
        widget=forms.widgets.FileInput(
            attrs={
                "class": "fa fa-image"
            }
        )
    )
    
    class Meta:
        model = Post_content
        fields = ('content','image',)
        
        
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
    