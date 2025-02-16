from django.urls import path
from .views import home
from .views import calculate_average_salary
from .views import job_search

urlpatterns = [
    path("", home, name="home"),
    path("search/", job_search, name="search_jobs"),
    #path("search/", search_jobs, name="search_jobs"),
    path("average-salary/", calculate_average_salary, name="average_salary"),

]
