from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pymongo

# MongoDB Connection
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["job_database"]
collection = db["python_jobs"]

# Initialize WebDriver
driver = webdriver.Chrome()
driver.get("https://www.linkedin.com/jobs/search/?keywords=python%20developer")

time.sleep(5)  # Allow time for page to load

# Find all job elements
jobs = driver.find_elements(By.CLASS_NAME, "job_seen_beacon")  # Corrected class for Indeed jobs
print(f"Found {len(jobs)} jobs")

job_list = []
for job in jobs[:10]:  # Scrape first 10 jobs
    try:
        title = job.find_element(By.CLASS_NAME, "jobTitle").text
        company = job.find_element(By.CLASS_NAME, "companyName").text
        location = job.find_element(By.CLASS_NAME, "companyLocation").text
        link = job.find_element(By.TAG_NAME, "a").get_attribute("href")

        job_data = {
            "title": title,
            "company": company,
            "location": location,
            "link": link
        }
        job_list.append(job_data)
    except Exception as e:
        print("Error scraping a job:", e)

# Store in MongoDB
if job_list:
    collection.insert_many(job_list)
    print("Job data scraped and stored in MongoDB.")
else:
    print("No jobs found!")

driver.quit()
