# Starting the browser
from bs4 import BeautifulSoup
import pandas as pd
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
time.sleep(2)

# Let's extract data by creating some empty list to store
titles = []
upvotes=[]
authors = []

content = driver.page_source
soup = BeautifulSoup(content, features="html.parser")

div = soup.find_all('div',attrs={'class': 'rpBJOHq2PR60pnwJlUyP0'})

for i in div:
    title = i.find('h3', attrs={'class':'_eYtD2XCVieq6emjKBH3m'})
    upvote = i.find('div', attrs={'class': '_1rZYMD_4xY3gRcSS3p8ODO _3a2ZHWaih05DgAOtvu6cIo '})
    author = i.find('a', attrs={'class': '_2tbHP6ZydRpjI44J3syuqC'})
    titles.append(title.text)
    upvotes.append(upvote.text)
    authors.append(author.text)

#save in csv
df = pd.DataFrame({'Post title': titles, 'Author': authors, 'Number of upvotes': upvotes})
df.to_csv('posts.csv', index=False, encoding='utf-8')


time.sleep(3)
driver.quit()