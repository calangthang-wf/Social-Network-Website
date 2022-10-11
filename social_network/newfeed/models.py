from distutils.command.upload import upload
from email.mime import image
from email.policy import default
from importlib.metadata import requires
from pyexpat import model
from turtle import title
from django.db import models
from django.utils import timezone

class Post_content(models.Model):
    content = models.TextField(max_length=5000, blank=False, null=False)
    image = models.ImageField(upload_to = "image", blank=True)
    time_create = models.DateTimeField(default=timezone.datetime.now())
    
    def __str__(self):
        return self.content
    

    
    
    
        
    