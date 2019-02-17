from django.shortcuts import render


def news_index(request):
    return render(request, 'news/index.html')


def search_index(request):
    return render(request, 'news/search.html')


# Create your views here.
