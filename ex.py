#This website is originally Turkish job apply site so some terms and words can be Turkish.


from bs4 import BeautifulSoup
import requests


#This function's aim is that get more information url and combine previous url after that go to another web tab and get the experience status.
def getExperienceText(url):
    more_info_html = requests.get(url).text
    soup2 = BeautifulSoup(more_info_html,'lxml')
    experiences= soup2.find_all('div',class_='detail mb-3 mb-sm-0 flex-sm-column')
    for experience in experiences:
        #Searching for experience part
         if 'Pozisyon' in experience.h3.text or 'Tecrübe' in experience.h3.text or 'Position' in experience.h3.text or 'Experience' in experience.h3.text:
            experience_text=experience.p.text
            return experience_text


html_text = requests.get('https://www.kariyer.net/is-ilanlari/yazilim+gelistirme+muhendisi?pst=2016&pkw=yaz%C4%B1l%C4%B1m%20geli%C5%9Ftirme%20m%C3%BChendisi').text
soup = BeautifulSoup(html_text, 'lxml')



jobs = soup.find_all('a', class_='k-ad-card')

with open("jobs.txt","w") as file:
    for index,job in enumerate(jobs):

        #Relevant parts of the data I want
        job_title = job.find('span', class_='k-ad-card-title multiline')
        company_name = job.find('div', class_="subtitle").span
        location = job.find('span', class_='location')
        job_condition = job.find('div', class_='badge-item badge-item--default')
    


        #tha main part of website so we can combine with specific url
        more_info = job['href']
        more_info = "https://www.kariyer.net"+more_info
        

        #Call the function and return the experience information
        experience_text = getExperienceText(more_info)
                

        #check the data it may none
        job_title_text = job_title.text if job_title else 'No title'
        company_name_text = company_name.text if company_name else 'No company name'
        location_text = location.text if location else 'No location'
        job_condition_text = job_condition.span.text if job_condition else 'No condition'
        more_info_text = more_info if more_info else 'No more information'
        experience_text_check=experience_text if experience_text else 'No experience status'

        #For writing to txt file
        file.write(f"Job #{index+1}\n")
        file.write("Company Name: " + company_name_text + "\n")
        file.write("Job Title: " + job_title_text + "\n")
        file.write("Location: " + location_text + "\n")
        file.write("Job Condition: " + job_condition_text + "\n")
        file.write("More info: " + more_info + "\n")
        file.write("Experience status: " + experience_text.strip() + "\n\n")


        
print("It's successfully done you can find and check jobs from jobs.txt")