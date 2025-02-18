# Copy this code to models.py
from django.db import models

class Job(models.Model):
    title = models.CharField(max_length=200)
    company = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    salary = models.CharField(max_length=200)
    scraped_date = models.DateTimeField()

    def __str__(self):
        return f"{self.title} at {self.company}"

    class Meta:
        ordering = ['-scraped_date']