from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import random
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:\development\chromedriver_win32\chromedriver.exe"
s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s)

driver.get("https://orteil.dashnet.org/cookieclicker/")

game_on = True
n_ = random.random()

while game_on:
    for n in range(0, 10000):
        click_me = driver.find_element(By.XPATH, '//*[@id="bigCookie"]')
        click_me.click()
        time.sleep(n_)
    game_on = False
    driver.quit()





