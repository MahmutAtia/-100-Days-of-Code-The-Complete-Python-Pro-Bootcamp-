import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys



def signin(driver:webdriver):
    sign = driver.find_element_by_link_text("Sign in").click()
    user = driver.find_element_by_id("username").send_keys("mahmod02015@gmail.com")
    passw = driver.find_element_by_id("password")
    passw.send_keys(os.environ.get("mypass"))
    passw.send_keys(Keys.ENTER)