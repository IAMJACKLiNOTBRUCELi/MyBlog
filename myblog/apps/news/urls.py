from django.urls import path
from news import views


app_name = 'news'

urlpatterns = [
    path('news/', views.news_index, name='index'),
    path('search/', views.search_index, name='search'),
]