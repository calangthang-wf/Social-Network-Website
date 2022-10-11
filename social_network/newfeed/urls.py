from urllib.parse import urlparse
from django.urls import path
from . import views

app_name = "newfeed"

urlpatterns = [
    path('', views.newFeed, name="newfeed"),
    path('add/', views.add_Post, name="addPost"),
    path('save/', views.save_Post, name="savePost"),
    path('404/', views.error, name='cocl'),
]
