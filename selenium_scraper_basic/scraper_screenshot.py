# Starting the browser
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

options = Options()
options.headless = True
options.add_argument("--window-size=1920,1080")

# Locating specific data
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.reddit.com/r/learnprogramming/top/?t=month")
time.sleep(3)

# set the google chrome window size
from selenium.webdriver.chrome.options import Options
options = Options()
options.add_argument("--window-size=1920,1080")

#taking screenshot
driver.save_screenshot('screenshot.png')


time.sleep(3)
driver.quit()