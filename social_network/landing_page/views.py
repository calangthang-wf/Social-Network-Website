import re
from django.shortcuts import render
from django.http import HttpResponse

def newFeed(request):
    return render(request, 'pages/newfeed.html')

