# importing needed library
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd

# for storing

position = []
link = []
name_of_company = []
experince = []
package = []
location = []
skills = []
rating = []
review = []
job_descrption = []

start_time = time.time()


# defining function

# for changing link    https://www.naukri.com/data-science-jobs-2
def changing_link(page_link, lt):
    # lt-->[0,0,1] flag,count,reload
    print(lt[2])
    lt[2] = lt[2] + 1
    if lt[0] == 0:
        lt[0] = 1
        lt[1] = 2
        return page_link
    else:
        p_link = page_link +'-'+ str(lt[1])
        lt[1] = lt[1] + 1
        return p_link


# for scrapping
def scraping(page_link, lt):
    # changing link
    page_link = changing_link(page_link, lt)
    if lt[2]==547:
        return
    driver.get(page_link)
    time.sleep(10)
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    # sara kaam scrapping wala
    if soup:
        jobs = soup.find_all('article', class_='jobTuple')
        for job in jobs:
            name = job.find('a', {'class': 'title ellipsis'})
            position.append(name.text.strip())
            link.append(name.get('href'))
            company = job.find('div', {'class': 'companyInfo subheading'})
            c = company.find_all('a')
            name_of_company.append(c[0].text.strip())
            try:
                reviews = c[1].find('span', class_='reviewsCount fleft').text.strip().split()[0]
                ratings = c[1].find('span', class_='starRating fleft').text.strip()
                review.append(reviews)
                rating.append(ratings)
            except:
                review.append(np.nan)
                rating.append(np.nan)
            job_d = job.find('ul', class_='')
            exp = job_d.find('span', {'class': 'ellipsis fleft expwdth'})
            try:
                experince.append(exp.get('title'))
            except:
                experince.append(np.nan)
            amount = job_d.find('li', {'class': 'fleft br2 placeHolderLi salary'})
            try:
                package.append(amount.text.strip())
            except:
                package.append(np.nan)
            l = job_d.find('span', class_='ellipsis fleft locWdth')
            try:
                location.append(l.text.strip())
            except:
                location.append(np.nan)
            s = job.find('div', class_='ellipsis job-description')
            try:
                job_descrption.append(s.text.strip())
            except:
                job_descrption.append(np.nan)
            try:
                tags = job.find('ul', {'class': 'tags has-description'})
                all_skill = tags.find_all('li', {'class': 'fleft dot'})
                temp = []
                for t in all_skill:
                    temp.append(t.text.strip())
                skills.append(temp)
            except:
                skills.append(np.nan)

# calling function
if __name__ == "__main__":
    opt = Options()
    opt.add_experimental_option('detach', True)
    opt.add_argument('--incognito')
    path = "/Users/abhijeetkashyap/Desktop/chromedriver"
    service = Service(executable_path=path)
    # opening chrome
    driver = webdriver.Chrome(service=service, options=opt)
    page_link = 'https://www.naukri.com/data-science-jobs'

    # ist-->flag,count,reload
    lt = [0, 0, 1]
    while (lt[2]<547):
        scraping(page_link, lt)

# converting into data frame

# creating dictionary
data={
    'Job-title':position,
    'Company':name_of_company,
    'Package(P/A)':package,
    'Experince':experince,
    'Skills': skills,
    'Job_Description':job_descrption,
    'Rating':rating,
    'Reviews':review,
    'Location': location,
    'Link-of-job': link
}
df = pd.DataFrame(data)

# saving into csv file
df.to_csv('jobs.csv')
end_time = time.time()
execution_time = end_time - start_time
print(execution_time)
