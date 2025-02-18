# Copy this code to urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.job_search, name='job_search'),
]