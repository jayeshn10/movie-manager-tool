from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import render, redirect
# Create your views here.

def loginuser(request):
    return render(request, 'login.html')

def registeruser(request):
    return render(request, 'register.html')

def logoutuser(request):
    logout(request)
    return redirect('login')

def home(request):
    return render(request,"index.html")

def movie(request):
    return render(request,"movie.html")

def Hello(request):
    return HttpResponse("Hello, Django!")

def video(request):
    return render(request,"video.html")