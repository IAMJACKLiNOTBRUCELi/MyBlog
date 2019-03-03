from django.shortcuts import render


def course_index(request):
    return render(request, 'course/course.html')


def course_detail(request):
    return render(request, 'course/course_detail.html')
# Create your views here.
