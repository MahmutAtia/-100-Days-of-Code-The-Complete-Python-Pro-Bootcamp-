from selenium import webdriver

driver = webdriver.Chrome()
url = "http://secure-retreat-92358.herokuapp.com/"
wiki = driver.get(url)
fname = driver.find_element_by_name("fName")
fname.send_keys("Mahmoud")
lname = driver.find_element_by_name("lName")
lname.send_keys("Atia")
email = driver.find_element_by_name("email")
email.send_keys("mahmod02015@gmail.com")
sign = driver.find_element_by_class_name("btn")
sign.click()
