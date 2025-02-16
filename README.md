# Job Scraper Project

## Overview
This project is a **job scraper** that extracts job listings for **Python Developers** from LinkedIn (and originally Indeed, but it has Cloudflare protection). 
The scraped job data is stored in a **MongoDB database** and can be managed via a **Django Admin Panel**. 
Users can **search, edit, and delete** job listings from the database.

## Features
- **Scrape job listings** from LinkedIn using Selenium.
- **Store scraped data** in MongoDB.
- **Django Admin Panel** for managing job listings.
- **Authentication** using Google Login for the admin panel.
- **Calculate the average salary** for Python Developers using NumPy.

---

## Setup Guide

### 1. Clone the Repository
```cmd
git clone https://github.com/yourusername/job_scraper_project.git
cd job_scraper_project
```

### 2. Install Dependencies
```cmd
pip install -r requirements.txt
```
Ensure you have **MongoDB** installed and running.

### 3. Configure MongoDB Connection
In `scraper.py`, update the connection:
```python
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["job_database"]
collection = db["python_jobs"]
```

### 4. Run the Scraper
```cmd
python jobapp/scraper.py
```
This will scrape job listings and store them in **MongoDB**.

### 5. Start Django Server
```cmd
python manage.py runserver
```
Now, open **http://127.0.0.1:8000/admin/** to manage job listings.

---

## File Structure
```
job_scraper_project/
│── job_project/           # Main Django Project
│   ├── settings.py       # Django Settings
│   ├── urls.py           # URL Routing
│   ├── wsgi.py           # WSGI Configuration
│
│── jobapp/               # Job Scraper App
│   ├── scraper.py        # Scrapes job data
│   ├── models.py         # Job Model for Database
│   ├── views.py          # API Views
│   ├── urls.py           # App Routing
│
│── templates/            # HTML Templates for Admin Panel
│── db.sqlite3            # Django Database (if using SQLite)
│── manage.py             # Django Command-Line Utility
│── requirements.txt      # Dependencies
│── README.md             # Project Documentation
```

---

## Usage
1. **Scrape Jobs**: Run `scraper.py` to collect job data.
2. **View Jobs**: Open MongoDB and run:
   ```cmd
   mongo
   use job_database
   db.python_jobs.find().pretty()
   ```
3. **Manage Jobs**: Use Django Admin to search, edit, or delete jobs.

---

## Future Enhancements
- Improve **data parsing** for better job detail extraction.
- Add **pagination** to scrape more job listings.
- Implement **automatic job updates** using a scheduler.
- Enhance **UI for job search** instead of using the Django Admin panel.

---

 **Karan Sahani**


