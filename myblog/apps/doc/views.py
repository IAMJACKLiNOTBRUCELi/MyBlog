from django.shortcuts import render


def doc_index(request):
    return render(request, 'doc/docDownload.html')
# Create your views here.
