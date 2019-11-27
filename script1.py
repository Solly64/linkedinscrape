import parameters
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import csv
from parsel import Selector
import urllib3 
df1=[]
df2=[]
df3=[]
df4= []
df5= []
# defining new variable passing two parameters
# writer = csv.writer(open(linked, 'wb'))

# # writerow() method to the write to the file object
# writer.writerow(['Name', 'Job Title', 'Company', 'College', 'Location', 'URL'])


# specifies the path to the chromedriver.exe
driver = webdriver.Chrome('C:/Users/Owner/Desktop/chromedriver.exe')

# driver.get method() will navigate to a page given by the URL address
driver.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')

# locate email form by_class_name
username = driver.find_element_by_id('username')
username.send_keys(parameters.linkedin_username)


# sleep for 0.5 seconds
sleep(0.5)

# send_keys() to simulate key strokes
# username.send_keys('srichberg2188@gmail.com')

# locate password form by_class_name
password = driver.find_element_by_id('password')
password.send_keys(parameters.linkedin_password)

# send_keys() to simulate key strokes
# password.send_keys('blue43')

# sleep for 0.5 seconds
sleep(0.5)

# locate submit button by_class_id
log_in_button = driver.find_element_by_class_name('from__button--floating')


# .click() to mimic button click
log_in_button.click()
for i in range(10):
    driver.get('https:www.google.com')
    sleep(3)

    search_query = driver.find_element_by_name('q')
    search_query.send_keys('site:linkedin.com/in/ AND "python developer" AND "Florida"' + 'page'+ ' ' + str(i))
    sleep(0.5)

    search_query.send_keys(Keys.RETURN)
    sleep(3)
    
    linkedin_urls = driver.find_elements_by_class_name('iUh30')
    linkedin_urls = [url.text for url in linkedin_urls]
    linkedin_urls=[i.split(' ', 2)[2] for i in linkedin_urls]
    print(linkedin_urls)
    sleep(0.5)



    driver.get('https://linkedin.com/in/mani-kandukuri-040409139/')
    
    driver.page_source
    # continuing on from before
    ...
    #linkedin_urls = [url.text for url in linkedin_urls]
    sleep(0.5)


# For loop to iterate over each URL in the list
    for linkedin_url in linkedin_urls:
       # get the profile URL 
        driver.get('https://www.linkedin.com/in/'+ linkedin_url)
    
       # add a 5 second pause loading each URL
        sleep(5)
    
       # assigning the source code for the webpage to variable sel
        sel = Selector(text=driver.page_source) 
     
    # terminates the application
    
    #xpath to extract the first h1 text 
        print('\n')
        name = sel.xpath('//*[starts-with(@class,"inline t-24 t-black t-normal break-words")]/text()').extract_first() 
        if name:
            name = name.strip()
            print('Name: ' +name)
            df1.append(name)
        job_title = sel.xpath('//h2/text()').extract_first()
        if job_title:
            job_title = job_title.strip()
            print('Job Title: ' + job_title)
            df2.append(job_title)
        location = sel.xpath('//*[starts-with(@class,"t-16 t-black t-normal inline-block")]/text()').extract_first()
    
        if location:
           location = location.strip()
           print('Location: '+ location)
           df3.append(location)
        employer = sel.xpath('//*[starts-with(@class,"text-align-left ml2 t-14 t-black t-bold full-width lt-line-clamp lt-line-clamp--multi-line ember-view" )]/text()').extract_first()
    
        if employer:
           employer = employer.strip()
           print('Company: ' + employer)
           df4.append(employer)
        education = sel.xpath('//*[starts-with(@id,"ember96" )]/text()').extract_first()
    
        if education:
           education = education.strip()
           print('College: ' + education)
           df5.append(education)
        print('URL: '+ 'https://www.linkedin.com/in/'+ linkedin_url)
        print('\n')
        
        linkedin_url = driver.current_url
    
    import pandas as pd
    
    linkedin=pd.DataFrame([df1,df2,df3,df4,df5])
    linkedin.to_csv('auto_link10.csv')