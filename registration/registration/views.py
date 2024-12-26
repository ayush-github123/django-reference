from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

def index(request):
    return render(request, 'index.html')


def registration(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return redirect('registration')
        
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists')
            return redirect('registration')


        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return redirect('registration')
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            messages.success(request, 'User created successfully')
            return redirect('login')
        
    return render(request, 'registration.html')
        

        
        
