from django.shortcuts import render

from django.http import HttpResponse
from datetime import datetime

from meetings.models import Meeting

def welcome(request):
    return render(request, "website/welcome.html",
                  {"meetings": Meeting.objects.all()})

def date(request):
    return HttpResponse("This page was served at " + str(datetime.now()))

def about(request):
    return HttpResponse("Hello, my name is Jacob, and this is my first Django site!")