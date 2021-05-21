from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.http import HttpResponseRedirect
from django.contrib import messages

# Create your views here.


def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        if User.objects.all().filter(username=username).exists():
            messages.info(request, 'Username Already Taken')
            print('username taken')
            return redirect('register')
        elif User.objects.all().filter(email=email).exists():
            messages.info(request, 'email Already Registered')
            return redirect('register')
        else:
            user = User.objects.create_user(
                username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
            user.save()
            print(user)
        return redirect('login')

    else:
        return render(request, 'accounts/register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')
