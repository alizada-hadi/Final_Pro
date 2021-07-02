from django.shortcuts import render
from django import views


def index(request):
    return render(request, "base.html")
