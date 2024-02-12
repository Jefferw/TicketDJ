from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"Authentication/index.html")

def signup(request):
    return render(request, "Authentication/signup.html")

def signin(request):
    return render(request, "Authentication/signin.html")

def signout(request):
    return render(request, "Authentication/signout.html")