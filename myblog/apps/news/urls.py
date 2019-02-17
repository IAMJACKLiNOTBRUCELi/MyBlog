from django.urls import path
from news import views


app_names = 'news'

urlpatterns = [
    path('news/', views.index, name='index'),
]