
from operator import attrgetter
from tkinter import Widget
from unicodedata import name
from django import forms
from .models import Post_content, Post_comment
from django.contrib.auth.models import User

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
    
    

