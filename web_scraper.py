import requests
from bs4 import BeautifulSoup

page = requests.get(
    "https://www.eluta.ca/search?q=software+developer&l=toronto&qc=")
soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find(id="container")
job_list = results.find(id="organic-jobs")
jobs_odd = job_list.find_all(class_="organic-job odd")
jobs_even = job_list.find_all(class_="organic-job even")
jobs = jobs_odd + jobs_even

for job in jobs:
    title_elem = job.find(class_="title")
    company_elem = job.find(class_="employer lk-employer")
    location_elem = job.find(class_="location")
    link_elem = job.find("a", class_="lk-job-title")["href"]

    title = title_elem.text.strip()
    company = company_elem.text.strip()
    location = location_elem.text.strip()

    print("--------------------------------------")
    print("Position:")
    print(title)

    print("\nCompany:")
    print(company)

    print("\nLocation:")
    print(location)

    print("\nApply Here:")
    #print(link)
    
