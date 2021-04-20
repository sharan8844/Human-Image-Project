from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import parameters 
from urllib.parse import urlparse

def is_url(url):
  try:
    result = urlparse(url)
    return True
  except ValueError:
    return False
driver = webdriver.Chrome('.../chromedriver') #enter path of chromedriver
driver.get('https://www.linkedin.com')

username = driver.find_element_by_name('session_key')
username.send_keys(parameters.linkedin_username)
sleep(0.5)
password = driver.find_element_by_name('session_password')
password.send_keys(parameters.linkedin_password)
sleep(0.5)
sign_in_button = driver.find_element_by_xpath('//*[@id="main-content"]/section[1]/div[2]/form/button')
sign_in_button.click()
sleep(0.5)

k=0
for query in parameters.search_query:
    driver.get('https:www.google.com')
    sleep(2.0)
    search_query = driver.find_element_by_name('q')
    search_query.send_keys(query)
    sleep(0.5)

    search_query.send_keys(Keys.RETURN)
    sleep(1.5)
    #import numpy as np
    urls = []
    for i in range(1,11):
        urll = driver.find_element_by_xpath('//*[@id="rso"]/div/div['+str(i)+']/div/div[1]/a').get_attribute("href")
        urls.append(urll)
    sleep(1.5)
    print('******************')
    print(urls)
    # //*[@id="rso"]/div/div[1]/div/div[1]/a
    # //*[@id="rso"]/div/div[2]/div/div[1]/a
    # //*[@id="rso"]/div/div[1]/div/div[1]/a
    for url in urls:
        driver.get(url)
        sleep(1.5)
        flag=0
        try:
            img = driver.find_element_by_xpath('//*[@id="ember48"]')
        except:
            flag=1
         
        if flag == 1:
            flag=0
            try:    
                img = driver.find_element_by_xpath('//*[@id="ember49"]') 
            except:
                flag=1   
        if flag==1:
            try:
                img = driver.find_element_by_xpath('//*[@id="ember50"]')   
            except:
                continue
              
        sleep(1.5)    
        src = img.get_attribute('src')
        print(type(src))
        typo = type(src)
        if typo != str:       
            continue       
        if is_url(src):
            driver.get(src)
            sleep(1.5)
        else:
            continue
        driver.find_element_by_xpath('/html/body/img').screenshot('../major project/images/Indian/'+str(k)+'.png') 
        #enter path of folder where images will be saved above
        k=k+1

driver.quit()

# /html/body/div[7]/div[3]/div/div/div/div/div[2]/div/div/main/div/div[1]/section/div[2]/div[1]/div[1]/div/div/img
# /html/body/div[8]/div[3]/div/div/div/div/div[2]/div/div/main/div/div[1]/section/div[2]/div[1]/div[1]/div/div/img
# //*[@id="ember49"]
# //*[@id="ember49"]
# //*[@id="ember49"]
# //*[@id="ember50"]
