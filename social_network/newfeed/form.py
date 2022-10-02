
from django import forms
from .models import Post_content

class PostForm(forms.ModelForm):
    class Meta:
        model = Post_content
        fields = ('content','image',)