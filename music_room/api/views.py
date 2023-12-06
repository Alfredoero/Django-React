"""
Views File for API app
"""
from django.http import HttpResponse
from .models import Room
# Create your views here.


def main(request):
    """ First End Point """
    rooms = Room.objects.all()
    return HttpResponse(rooms)
