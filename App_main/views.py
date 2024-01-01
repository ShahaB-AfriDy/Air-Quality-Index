from django.shortcuts import render

# Create your views here.

def Home(request):
    return render(request,template_name="home.html")

def About(request):
    return render(request,template_name="about.html")