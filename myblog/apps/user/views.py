from django.shortcuts import render


def register_index(request):
    return render(request, 'users/register.html')


def login_index(request):
    return render(request, 'users/login.html')
# Create your views here.
