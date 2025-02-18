# Copy this code to views.py
from django.shortcuts import render
from django.db.models import Q
from .models import Job

def job_search(request):
    query = request.GET.get('q')
    jobs = Job.objects.all()
    
    if query:
        jobs = jobs.filter(
            Q(title__icontains=query) |
            Q(company__icontains=query) |
            Q(location__icontains=query)
        )
    
    return render(request, 'jobs/job_list.html', {'jobs': jobs})