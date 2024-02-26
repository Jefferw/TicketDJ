from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User 
from django.contrib import messages
from django.db import connection
from django.contrib.auth import login
# Create your views here.
def home(request):
    return render(request,"Authentication/index.html")

def signup(request):
    if request.method == "POST":
        user_data = {
            'email': request.POST.get('email'),
            'phone_number': request.POST.get('phone_number'),
            'password': request.POST.get('password'),
            'first_name': request.POST.get('first_name'),
            'last_name': request.POST.get('last_name'),
            'user_status': request.POST.get('user_status'),
            'affiliation': request.POST.get('affiliation'),
        }

        messages.success(request, "Your account has been created successfully.")

        return redirect('signup')

    return render(request, "Authentication/signup.html")

def signin(request):
    current_user=None
    if request.method == "POST":
        login_data = {
            'email': request.POST.get('email'),
            'password': request.POST.get('password'),
        }
        user_pass = read_user(login_data['email'])[3]
        if(user_pass == login_data['password']):
            messages.success(request, "Successfully Logged In")
            user_email = login_data['email']
            print("Successfully Logged In")
            return redirect('home')
        else:
            messages.error(request, "Invalid Login")
            print("Invalid Login")
    return render(request, "Authentication/signin.html")


def signout(request):
    return render(request, "Authentication/signout.html")


"""GENERAL USE SQL QUERIES"""
def create_user(user_data):
    with connection.cursor() as cursor:
        # Create a new user
        cursor.execute("""
            INSERT INTO Helpdesk_User
            (user_id, email, phone_number, password, first_name, last_name, user_status, affiliation)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s);
        """, (user_data['email'], user_data['phone_number'], 
              user_data['password'], user_data['first_name'], user_data['last_name'],
              user_data['user_status'], user_data['affiliation']))
        
    return user_data


def read_user(email):
    with connection.cursor() as cursor:
        # Read a specific user by email address
        cursor.execute("SELECT * FROM Helpdesk_User WHERE email = %s;", [email])
        user = cursor.fetchone()
    return user


def update_user(email, phone_number=None, password=None, first_name=None, last_name=None, user_status=None, affiliation=None):
    with connection.cursor() as cursor:
        # Update phone number
        if phone_number is not None:
            update_phone_number = """
                UPDATE Helpdesk_User
                SET phone_number = %s
                WHERE email = %s;
            """
            cursor.execute(update_phone_number, [phone_number, email])

        # Update password
        if password is not None:
            update_password = """
                UPDATE Helpdesk_User
                SET password = %s
                WHERE email = %s;
            """
            cursor.execute(update_password, [password, email])

        # Update first name
        if first_name is not None:
            update_first_name = """
                UPDATE Helpdesk_User
                SET first_name = %s
                WHERE email = %s;
            """
            cursor.execute(update_first_name, [first_name, email])

        # Update last name
        if last_name is not None:
            update_last_name = """
                UPDATE Helpdesk_User
                SET last_name = %s
                WHERE email = %s;
            """
            cursor.execute(update_last_name, [last_name, email])

        # Update user status
        if user_status is not None:
            update_user_status = """
                UPDATE Helpdesk_User
                SET user_status = %s
                WHERE email = %s;
            """
            cursor.execute(update_user_status, [user_status, email])

        # Update affiliation
        if affiliation is not None:
            update_affiliation = """
                UPDATE Helpdesk_User
                SET affiliation = %s
                WHERE email = %s;
            """
            cursor.execute(update_affiliation, [affiliation, email])

    # Return the updated user
    return read_user(email)

def delete_user(email):
    with connection.cursor() as cursor:
        # Delete a user by email address
        cursor.execute("DELETE FROM Helpdesk_User WHERE email = %s;", [email])

def get_all_users():
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM Helpdesk_User;")
        rows = cursor.fetchall()
