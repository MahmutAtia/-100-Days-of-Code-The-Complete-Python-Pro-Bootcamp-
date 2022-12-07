import pytube
import requests
from selenium import webdriver

driver = webdriver.Chrome()
site = driver.get("https://pytube.io/en/latest/")
v = driver.find_element_by_css_selector(".reference internal")


list= ["buyCursor", "buyGrandma","buyFactory", "buyMine","buyShipment", "buyAlchemy lab", "buyPortal","buyTime machine"]
buy_C = driver.find_element_by_id(list[0])
buy_G = driver.find_element_by_id(list[1])

now  = dt.datetime.now()

cookie_elem.click()
print()
if now.second % 5 == 0:
    # def check
    money = driver.find_element_by_id("money").text
    if int(money) > 100:
        buy_G.click()
    else:
        try:
            buy_C.click()
        except:
            pass