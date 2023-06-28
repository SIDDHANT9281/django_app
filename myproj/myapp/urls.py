from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    # Add more URL patterns for your app here
]