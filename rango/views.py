from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says hey partner!")

# Create your views here.
def about(request):
    return HttpResponse("Rango says here is the about page")