from distutils.command.upload import upload
from email.mime import image
from django.db import models
from django.utils import timezone

class Post_content(models.Model):
    content = models.TextField(max_length=5000, blank=False, null=False)
    image = models.ImageField(upload_to = "")
    
    
    
        
    