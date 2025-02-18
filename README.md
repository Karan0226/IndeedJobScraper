# Job Scraper

## 📌 Overview
A web application that scrapes **Python Developer** job listings from **Indeed.com** and provides salary analysis.

## 🚀 Features
- ✅ Web scraping of **Indeed.com** job listings
- ✅ Stores job data in **MongoDB**
- ✅ Provides a **Django Admin Panel** for job management
- ✅ Salary analysis using **NumPy and Pandas**
- ✅ Interactive web interface

---

## 🛠️ Setup Instructions

### **1️⃣ Create & Activate Virtual Environment**
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### **2️⃣ Install Dependencies**
```bash
pip install -r requirements.txt
```

### **3️⃣ Set Up Environment Variables**
Create a `.env` file in the project directory with the following:
```plaintext
MONGODB_URI=your_mongodb_uri
SECRET_KEY=your_django_secret_key
```

### **4️⃣ Run Database Migrations**
```bash
python manage.py migrate
```

### **5️⃣ Create a Superuser (For Admin Panel)**
```bash
python manage.py createsuperuser
```

### **6️⃣ Start Django Server**
```bash
python manage.py runserver
```

---

## 📊 Salary Analysis
The salary analysis notebook is available in the `analysis/` folder.

Run the analysis:
```bash
jupyter notebook analysis/salary_analysis.ipynb
```

---

## 🔧 Deployment Instructions
To deploy this project:
1. **Use Gunicorn & Nginx for hosting.**
2. **Set up MongoDB Atlas for cloud storage.**
3. **Configure Django settings for production (`DEBUG=False`).**

---

## 🤝 Contributing
Contributions are welcome! Feel free to submit **pull requests** or open **issues** for feature requests.

---

## 🛠 Tech Stack
- **Python** (Django, Selenium, NumPy)
- **MongoDB** (Data Storage)
- **Selenium WebDriver** (Web Scraping)
- **HTML, CSS, JavaScript** (Frontend)

---


