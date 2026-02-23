from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

def register_view(request):
    if request.method == "POST":
        data = request.POST
        User.objects.create_user(username=data['username'], password=data['password'])
        return redirect('/login/')
    return render(request, 'register.html')

def login_view(request):
    if request.method == "POST":
        data = request.POST
        user = authenticate(username=data['username'], password=data['password'])
        if user:
            login(request, user)
            return render(request, 'welcome.html')
        else:
            return render(request, 'fail.html')
    return render(request, 'login.html')