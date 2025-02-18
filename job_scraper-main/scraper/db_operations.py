from pymongo import MongoClient
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

def get_database():
    client = MongoClient(os.getenv('MONGODB_URI'))
    return client['job_database']

def insert_jobs(jobs):
    db = get_database()
    jobs_collection = db['jobs']
    
    for job in jobs:
        # Update if exists, insert if not
        jobs_collection.update_one(
            {'source_url': job['source_url']},
            {'$set': job},
            upsert=True
        )
    
    return len(jobs)
