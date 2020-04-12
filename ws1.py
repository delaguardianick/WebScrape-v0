# prints the title, company and location of indeed's search result.

import requests
import pprint
from bs4 import BeautifulSoup
import re


title = input('What do you wanna search for: ')
title = title.replace(' ', '+')

location = input("Location: ")
location = location.replace(' ', '+')

URL = 'https://ca.indeed.com/jobs?q=%s&l=%s&radius=5' % (title, location)
print(URL)
# URL = 'https://ca.indeed.com/jobs?q=developer+intern&l=toronto&radius=5'
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='resultsCol')

job_elems = results.find_all('div', class_="jobsearch-SerpJobCard")
count = 0

jobTitle_list = []
jobCompany_list = []
jobLocation_list = []
jobLink_list = []
# You dont have to specifiy which class is inside what
# It looks for the class inside the whole html

for job_elem in job_elems:
    title_elem = job_elem.find('div',class_="title")
    jobTitle = title_elem.text.strip()
    jobTitle_list.append(jobTitle)

    company_elem = job_elem.find('span', class_='company')
    jobCompany = company_elem.text.strip()
    jobCompany_list.append(jobCompany)

    location_elem = job_elem.find('span', class_='location')
    if location_elem != None:
        jobLocation = location_elem.text.strip()
        jobLocation_list.append(jobLocation)
    else:
        continue

    link_html = title_elem.find('a', href = True)
    jobLink = 'https://ca.indeed.com%s' % link_html['href']
    jobLink_list.append(jobLink)

    # if None in (title_elem, company_elem, location_elem, link_html ):
    #     continue

    count += 1
    print(str(count) + '.')
    print(jobTitle)
    print(jobCompany)
    print(jobLocation)
    print(jobLink)    


