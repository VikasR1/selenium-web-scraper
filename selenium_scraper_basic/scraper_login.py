# ! pip install selenium --upgrade --quiet
# ! pip install pandas --upgrade --quiet
# ! pip install bs4 --upgrade --quiet

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

#print the page source
# print(driver.page_source)

# Clicking on Log in button
login_button= driver.find_element(By.XPATH, '//*[@id="SHORTCUT_FOCUSABLE_DIV"]/div[1]/header/div/div[2]/div/div[1]/a[1]')
login_button.click()

# switch to login frame
login_frame = driver.find_element(By.XPATH,'/html/body/div/main/div[1]')
driver.switch_to_frame(login_frame)

# enter user name
username=driver.find_element(By.XPATH,'//*[@id="loginUsername"]')
username.send_keys('')
time.sleep(3)

#enter password
password = driver.find_element(By.XPATH,'//*[@id="loginPassword"]')
password.send_keys('')
time.sleep(3)

#enter submit button
submit = driver.find_element(By.XPATH,'/html/body/div/main/div[1]/div/div/form/fieldset[4]/button')
submit.click()

time.sleep(3)
driver.quit()