"""
This is the URLS file for the API app
"""
from django.urls import path

from .views import RoomView

urlpatterns = [
    path('', RoomView.as_view())
]
