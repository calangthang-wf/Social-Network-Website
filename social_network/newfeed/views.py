from ast import Return
from email.mime import image
import re
from turtle import home
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

from .models import Post_content
from .form import PostForm


def newFeed(request):
    data = { "posts": Post_content.objects.all().order_by('-time_create')} # get all post from database
    return render(request, 'pages/new_feed.html', data)



#creat post
def add_Post(request):
    add = PostForm()
    return render(request, "pages/post.html", { "f": add })  # add value for f = add

#save post
def save_Post(request):
    if request.method == "POST":
        saveP = PostForm(request.POST, request.FILES)  
        if saveP.is_valid():
            saveP.save()
            return redirect('http://127.0.0.1:8000')
        else:
            return render(request, 'pages/404.html')
    else:
        return render(request, 'pages/404.html')
    
def error(request):
    return render(request, 'pages/error.html')
    
    