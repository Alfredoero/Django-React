from django.shortcuts import render


def Index(request, *args, **kwargs):
    return render(request, "frontend/index.html")
