from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.db import IntegrityError
from django.contrib.auth.models import User, auth

def signup (request) :
    if request.method == 'POST' :
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            print("ERROR")
            messages.info(request, 'Sorry, this username is already taken. You can try again with another username.')
            return redirect('signup')
        else:
            user = User.objects.create_user(username=username, email=email, first_name=first_name, last_name=last_name, password=password)
            user.save()
            return redirect('/')
    else :
        return render(request, 'signup.html')