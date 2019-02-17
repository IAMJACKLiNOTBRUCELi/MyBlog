from django.shortcuts import render


def course_index(request):
    return render(request, 'course/course.html')
# Create your views here.
