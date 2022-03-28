from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


chrome_driver_path = "C:\development\chromedriver_win32\chromedriver.exe"

s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)

# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# number = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
# count_number = driver.find_element(By.CSS_SELECTOR, "#articlecount a")

# print(count_number.text)

# How to click on a link
# count_number.click()

# how to click on a link
# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# all_portals = driver.find_element(By.LINK_TEXT, "All portals")
# all_portals.click()


# how to fill a form using keys
# driver.get("https://en.wikipedia.org/w/index.php?search=&title=Special%3ASearch&go=Go")
# search_bar = driver.find_element(By.NAME, '//*[@id="searchButton"]')
# print(search_bar.text)


# how to use the keys words to fill up forms
# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# search = driver.find_element(By.NAME, "search")
# search.send_keys("python")
# search.send_keys(Keys.ENTER)



# How to fill up the form online using selenium

# driver.get("http://secure-retreat-92358.herokuapp.com/")
# f_name = driver.find_element(By.XPATH, '/html/body/form/input[1]')
# f_name.send_keys("Kodjostarts")
# f_name.send_keys(Keys.ENTER)
#
# l_name = driver.find_element(By.XPATH, '/html/body/form/input[2]')
# l_name.send_keys("Afante")
#
# email_place = driver.find_element(By.XPATH, '/html/body/form/input[3]')
# email_place.send_keys("kod.dodji@gmail.com")
# email_place.send_keys(Keys.ENTER)

# second try fiiling up forms/ subsciption
# driver.get("https://www.appbrewery.co/p/newsletter")
# email_place = driver.find_element(By.CLASS_NAME, "form-control")
# email_place.send_keys("kod.dodji@gmail.com")
#
# submit_bar = driver.find_element(By.NAME, "commit")
# submit_bar.send_keys(Keys.ENTER)
"""it is really great not to forget to use the ".click" function instead of the ".ENTER"  """


# driver.quit()

