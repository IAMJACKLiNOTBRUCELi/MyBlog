from django.urls import path
from user import views

app_name = 'user'

urlpatterns = [
    path('register/', views.register_index, name='register'),
    path('login/', views.login_index, name='login'),
]

