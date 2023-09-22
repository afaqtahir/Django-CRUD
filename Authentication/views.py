from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db import transaction
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def login_view(request):
    if request.method == "POST":
        form_data = request.POST
        user = User.objects.filter(username=form_data['username'])
        if not user.exists():
            messages.info(request, "Invalid Username")
            return redirect('/accounts/login/')

        user = authenticate(
            username=form_data['username'],
            password=form_data['password']
        )
        if user is None:
            messages.info(request, "Invalid Credentials")
            return redirect('/accounts/login/')
        else:
            login(request, user)
            return redirect('/recipes/')
    return render(request, "login.html")

def logout_view(request):
    logout(request)
    return redirect('/accounts/login/')
def register_view(request):
    if request.method == "POST":
        with transaction.atomic():
            form_data = request.POST

            user = User.objects.filter(username=form_data['username'])
            if user.exists():
                messages.error(request, "Username already exists")
                return redirect('/accounts/register/')

            user = User(
                first_name=form_data['first_name'],
                last_name=form_data['last_name'],
                username=form_data['username'],
            )
            user.set_password(form_data['password'])
            user.save()
            messages.info(request, "Your account is created, please proceed with login")
            return redirect('/accounts/login/')
    return render(request, "register.html")
