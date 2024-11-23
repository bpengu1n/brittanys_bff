from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import pandas as pd

from time import sleep


cService = webdriver.ChromeService(executable_path='/opt/homebrew/bin/chromedriver')
driver = webdriver.Chrome(service = cService)

driver.get("https://archiveofourown.org")
sleep(2)
inputs = driver.find_elements(By.TAG_NAME, 'input')
inputs[0].click()
inputs[1].click()

driver.find_elements(By.TAG_NAME, 'button')[0].click()

anchors = {_.text: _ for _ in driver.find_elements(By.TAG_NAME, 'a')}

anchors['Anime & Manga'].click()

input()