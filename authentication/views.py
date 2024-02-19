from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User 
from django.contrib import messages
from django.db import connection
# Create your views here.
def home(request):
    return render(request,"Authentication/index.html")

def signup(request):
    if request.method == "POST":
        email = request.POST.get('email')
        phoneNumber = request.POST.get('phoneNumber')
        firstName = request.POST.get('firstName')
        lastName = request.POST.get('lastName')
        password = request.POST.get('password')

        newUser = User.objects.create(firstName+" "+lastName, email, password)
        newUser.phone_number = phoneNumber
        newUser.first_name = firstName
        newUser.last_name = lastName

        newUser.save()

        messages.success(request, "Your account has been created successfully.")

        return redirect('signup')

    return render(request, "Authentication/signup.html")

def signin(request):
    return render(request, "Authentication/signin.html")

def signout(request):
    return render(request, "Authentication/signout.html")

def test_query_view(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM Helpdesk_User;")
        rows = cursor.fetchall()

    return render(request, 'Authentication/test_query_view.html', {'rows': rows})