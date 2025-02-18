import requests
from bs4 import BeautifulSoup
import pymongo
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

class IndeedScraper:
    def __init__(self):
        self.client = pymongo.MongoClient(os.getenv('MONGODB_URI'))
        self.db = self.client['job_database']
        self.collection = self.db['jobs']

    def scrape_indeed(self, location):
        base_url = "https://www.indeed.com/jobs"
        params = {
            'q': 'Python Developer',
            'l': location,
            'sort': 'date'
        }
        
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }

        try:
            response = requests.get(base_url, params=params, headers=headers)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            jobs = []
            for job in soup.find_all('div', class_='job_seen_beacon'):
                title = job.find('h2', class_='jobTitle').text.strip()
                company = job.find('span', class_='companyName').text.strip()
                location = job.find('div', class_='companyLocation').text.strip()
                
                salary_elem = job.find('div', class_='salary-snippet')
                salary = salary_elem.text.strip() if salary_elem else 'Not specified'
                
                job_data = {
                    'title': title,
                    'company': company,
                    'location': location,
                    'salary': salary,
                    'scraped_date': datetime.now()
                }
                
                jobs.append(job_data)
                
            if jobs:
                self.collection.insert_many(jobs)
                print(f"Successfully scraped and stored {len(jobs)} jobs")
                
        except Exception as e:
            print(f"Error occurred: {str(e)}")