from django.shortcuts import render


def index(request):
    return render(request, 'news/index.html')
# Create your views here.
