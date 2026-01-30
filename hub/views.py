from django.shortcuts import render
from datetime import datetime

def home(request):
    return render(request, "hub/home.html", {"year": datetime.now().year})

def projects(request):
    return render(request, "hub/projects.html", {"year": datetime.now().year})

def about(request):
    return render(request, "hub/about.html", {"year": datetime.now().year})
