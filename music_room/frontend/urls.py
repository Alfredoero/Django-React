"""
This is the URLS file for the API app
"""
from django.urls import path

from .views import Index

urlpatterns = [
    path('', Index)
]