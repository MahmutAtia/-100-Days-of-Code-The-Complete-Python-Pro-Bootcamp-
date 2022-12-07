import random
import datetime as dt
from selenium import webdriver


url= "https://pytube.io/en/latest/"
driver = webdriver.Chrome()
driver.get(url)
v = driver.find_element_by_link_text("Quickstart")
print(v.get_attribute("href"))
