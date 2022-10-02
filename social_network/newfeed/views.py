from email.mime import image
import re
from django.shortcuts import render
from django.http import HttpResponse

from .models import Post_content
from .form import PostForm

def newFeed(request):
    return render(request, 'pages/new_feed.html')




def add_Post(request):
    add = PostForm()
    return render(request, "pages/new_feed.html", { "f": add })  # gan gia tri cho bien f = add


def save_Post(request):
    if request.method == "POST":
        saveP = PostForm(request.POST, request.FILES)
        if saveP.is_valid():
            saveP.save()
            return HttpResponse("Complete!")
        else:
            return HttpResponse("Error! Please, try again")
    else:
        return HttpResponse("Error 404!")