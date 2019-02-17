from django.urls import path
from doc import views

app_name = 'doc'

urlpatterns = [
    path('doc/', views.doc_index, name='index'),
]
