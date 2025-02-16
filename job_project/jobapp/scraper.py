# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from webdriver_manager.chrome import ChromeDriverManager

# def scrape_jobs():
#     # Set up Chrome options
#     chrome_options = Options()
#     chrome_options.add_argument("--disable-gpu")  # Disable GPU usage
#     chrome_options.add_argument("--headless=new")  # Run Chrome in headless mode

#     # Initialize WebDriver
#     service = Service(ChromeDriverManager().install())
#     driver = webdriver.Chrome(service=service, options=chrome_options)

#     # Open LinkedIn Jobs page
#     url = "https://in.indeed.com/jobs?q=python+developer"
#     driver.get(url)

#     # Wait for jobs to load
#     driver.implicitly_wait(5)

#     # Extract job listings (Modify this selector if needed)
#     jobs = driver.find_elements(By.CLASS_NAME, "base-card")  # Updated class name

#     job_list = []
#     for job in jobs:
#         job_list.append(job.text)  # Collect job details

#     driver.quit()
#     return job_list  # Return scraped jobs
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from webdriver_manager.chrome import ChromeDriverManager
# import time

# def scrape_jobs():
#     # Set up Chrome options
#     chrome_options = Options()
#     chrome_options.add_argument("--disable-gpu")
#     chrome_options.add_argument("--headless=new")  # Run in headless mode
#     chrome_options.add_argument("--window-size=1920,1080")  # Set full window size

#     # Initialize WebDriver
#     service = Service(ChromeDriverManager().install())
#     driver = webdriver.Chrome(service=service, options=chrome_options)

#     # Open LinkedIn Jobs page
#     url = "https://www.linkedin.com/jobs/search/?keywords=python%20developer"
#     driver.get(url)

#     # Wait for page to load
#     wait = WebDriverWait(driver, 10)
#     wait.until(EC.presence_of_element_located((By.CLASS_NAME, "base-card")))

#     # Scroll down to load more jobs
#     for _ in range(5):  # Adjust this number to load more jobs
#         driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
#         time.sleep(2)  # Wait for jobs to load

#     # Extract job listings
#     jobs = driver.find_elements(By.CLASS_NAME, "base-card")

#     job_list = []
#     for job in jobs:
#         try:
#             title = job.find_element(By.CLASS_NAME, "base-search-card__title").text
#             company = job.find_element(By.CLASS_NAME, "base-search-card__subtitle").text
#             location = job.find_element(By.CLASS_NAME, "job-search-card__location").text
#             link = job.find_element(By.TAG_NAME, "a").get_attribute("href")

#             job_list.append({
#                 "title": title,
#                 "company": company,
#                 "location": location,
#                 "link": link
#             })
#         except Exception as e:
#             print(f"Error extracting job: {e}")

#     driver.quit()
#     return job_list

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from pymongo import MongoClient
import time

# Your LinkedIn login credentials
LINKEDIN_EMAIL = "your_email@example.com"
LINKEDIN_PASSWORD = "your_password"

def scrape_jobs():
    chrome_options = Options()
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--headless=new")  # Remove this line if you want to see the browser
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)

    # Open LinkedIn login page
    driver.get("https://www.linkedin.com/login")
    time.sleep(3)

    # Enter email
    email_input = driver.find_element(By.ID, "username")
    email_input.send_keys(LINKEDIN_EMAIL)

    # Enter password
    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys(LINKEDIN_PASSWORD)
    password_input.send_keys(Keys.RETURN)

    time.sleep(5)  # Wait for login to complete

    # Now go to job search page
    url = "https://www.linkedin.com/jobs/search/?keywords=python%20developer"
    driver.get(url)
    time.sleep(5)

    jobs = driver.find_elements(By.CLASS_NAME, "job-card-container")

    job_list = []
    for job in jobs:
        try:
            title = job.find_element(By.CLASS_NAME, "job-card-list__title").text
            company = job.find_element(By.CLASS_NAME, "job-card-container__company-name").text
            location = job.find_element(By.CLASS_NAME, "job-card-container__metadata-item").text
            job_list.append({"title": title, "company": company, "location": location})
        except:
            continue

    driver.quit()

    # Connect to MongoDB and store data
    client = MongoClient("mongodb://localhost:27017/")
    db = client["job_scraper_db"]
    job_collection = db["jobs"]

    if job_list:
        job_collection.insert_many(job_list)
        print(f"{len(job_list)} jobs inserted into MongoDB.")
    else:
        print("No jobs found.")

scrape_jobs()
