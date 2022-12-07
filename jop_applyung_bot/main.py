import time

from signin import *

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import os

url = "https://www.linkedin.com/jobs/search/?currentJobId=3089177252&f_AL=true&f_WT=2&geoId=101282230&keywords=data&location=Germany&refresh=true"
driver = webdriver.Chrome()
driver.get(url= url)
signin(driver)
list = driver.find_elements_by_class_name("job-card-container")

num = 1
while True:
    time.sleep(5)
    try:
        apply = driver.find_element_by_class_name("jobs-apply-button")
        apply.click()
    except:
        if num < len(list):
            num+=1

    try:
        while True :
            next = driver.find_element_by_id("ember375").click()
            time.sleep(2)
        rew = driver.find_element_by_id("ember413").click()
        time.sleep(2)

        submit = driver.find_element_by_id("ember450").click()

    except:
        close = driver.find_element_by_class_name("artdeco-button__icon").click()
        time.sleep(2)
        discard = driver.find_element_by_css_selector(".artdeco-modal__actionbar button" ).click()
    finally :
        time.sleep(2)
        list[num].click()
        if num < len(list):
            num+=1
        else:
            break

