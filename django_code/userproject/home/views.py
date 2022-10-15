from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login

# Create your views here.
def index(request):
    render(request, 'index.html')

def login(request):
    render(request, 'login.html')

def logout(request):
    render(request, 'index.html')