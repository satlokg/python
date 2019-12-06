from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request, 'login.html',{'title':'user login'})

def register(request):
    return render(request, 'register.html',{'title':'user register'})
