from django.shortcuts import render

# Create your views here.

def Graphs(request):
    return render(request,template_name="graphs.html")