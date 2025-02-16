from django.shortcuts import render
from .models import Job
from .scraper import scrape_jobs

def home(request):
    return render(request, "home.html")

def job_search(request):
    jobs = scrape_jobs()  # Run the scraper
    #return JsonResponse({"jobs": jobs})
    return render(request, "jobapp/job_results.html", {"jobs": jobs})
    # query = request.GET.get("q")
    # if query:
    #     jobs = Job.objects.filter(title__icontains=query)
    # else:
    #     jobs = Job.objects.all()
    # return render(request, "search.html", {"jobs": jobs})


import numpy as np
from django.http import JsonResponse

def calculate_average_salary(request):

    jobs = Job.objects.filter(location__icontains="YourCity")  # Change 'YourCity' to your city name
    salaries = [int(job.salary) for job in jobs if job.salary.isnumeric()]
    
    if salaries:
        average_salary = np.mean(salaries)
    else:
        average_salary = 0
    
    return JsonResponse({"average_salary": average_salary})
