
# 💼 Naukri.com Job Scraper: Data Science Role Insights

## 🛠️ Tech Stack

- **Python**
- **Selenium** – for dynamic web browsing and scraping
- **BeautifulSoup** – for HTML parsing
- **Pandas** – for tabular data handling
- **NumPy** – for missing value handling

---

## 📊 Project Overview

This project is a **web scraper** built to collect detailed **Data Science job listings** from [Naukri.com](https://www.naukri.com/). The script scrapes multiple pages and compiles a comprehensive dataset with:

- 🧾 Job Descriptions  
- 🏢 Company Names  
- 💰 Salary Packages  
- 🎯 Experience Requirements  
- 🧠 Required Skills  
- 🌍 Location  
- 🌟 Ratings and Reviews  
- 🔗 Job URLs

This dataset is exported as `jobs.csv` for further analysis.

---

## 📂 Features Scraped

| Feature          | Description                                                    |
|------------------|----------------------------------------------------------------|
| Job Title        | Role name (e.g., Data Scientist, ML Engineer)                  |
| Company Name     | Hiring company                                                 |
| Package          | Annual salary offered                                          |
| Experience       | Experience required (e.g., 1-3 years, 5-10 years)              |
| Skills           | Tags/keywords from job description                             |
| Description      | Summary of responsibilities                                    |
| Rating & Reviews | Company rating and number of reviews                           |
| Location         | Job location (city/region)                                     |
| Job Link         | Direct URL to job post                                         |

---

## 📈 Use Cases

- 🔍 **Job Market Research**
- 🤖 **Build ML models** to predict salaries or required skills
- 📚 **Resume Matching Systems**
- 📊 **EDA on skill demand** across job roles
- 📍 **Salary benchmarks by experience and region**

---

## ⚙️ How It Works

1. **Browser Initialization**:  
   Opens Chrome in incognito mode using Selenium WebDriver.

2. **Dynamic Page Navigation**:  
   Visits and scrolls through multiple paginated links.

3. **HTML Parsing**:  
   Extracts job details using BeautifulSoup.

4. **Data Storage**:  
   Compiles data in lists → Converts to DataFrame → Saves as `jobs.csv`.

5. **Loop Until Final Page**:  
   Script iterates through pages until a fixed reload count is reached (e.g., 547).

---
