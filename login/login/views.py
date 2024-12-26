from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def index(request):
    return render(request, 'index.html')

def login_page(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return render(request, 'index.html')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})


    return render(request, 'login.html')

