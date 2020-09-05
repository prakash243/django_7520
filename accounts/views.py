from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
def index1(request):
    return render(request, 'account_home.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def register(request):
    
    return render(request, 'register.html')

def login(request):
    return render(request, 'login.html')

def logout(request):
    return render(request, 'logout.html')