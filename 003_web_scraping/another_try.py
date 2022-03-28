from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "C:\development\chromedriver_win32\chromedriver.exe"

s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)
# how to use selenium to extract the class name
driver.get("https://www.python.org/events/")

# how to go from another
# logo = driver.find_element(By.CSS_SELECTOR, "")
# how can we go from there to the tag name

# button = driver.find_element(By.CLASS_NAME, "download-buttons")
# print(button.text)


# one of the best search option is xpath
# we just need to get the xpath by a right click and copy the path
# price = driver.find_element(By.XPATH, "//*[@id='corePrice_desktop']/div/table/tbody/tr/td[2]/span[1]/span[2]")
# print(price.text)

# how to get elements and made a dictionary with them
event_titles = driver.find_elements(By.CLASS_NAME, "event-title")
# print(event_titles)
# title_list = [(title.text) for title in event_titles]
# print(title_list)


# HOW TOUSE SELENIUM TO CLICK ON STUFF THE INTERFACE
driver.get("https://www.python.org/events/")
event_times = driver.find_elements(By.CSS_SELECTOR, "time")

event_names = driver.find_elements(By.CSS_SELECTOR, "h3 a")

events = {}
for n in range(len(event_names)):
    events[n] = {
        "time": event_times[n].text,
        "name": event_names[n].text,
    }

print(events)

driver.quit()
