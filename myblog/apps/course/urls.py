from django.urls import path
from course import views


app_name = 'course'

urlpatterns = [
    path('course/', views.course_index, name='index'),
    path('CourseDetail/', views.course_detail, name='detail'),
]
