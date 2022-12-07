from selenium import webdriver

driver = webdriver.Chrome()
driver.get(url="https://www.python.org/")
events = driver.find_elements_by_css_selector(".event-widget li a")
times = driver.find_elements_by_css_selector(".event-widget time")

for event in events:
    print(event.text)
