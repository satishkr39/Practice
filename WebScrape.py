import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd

respone = requests.get("https://www.flipkart.com/search?q=laptop&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")
#driver  = webdriver.Chrome('C:\chromedriver_win32\chromedriver.exe')

#driver.get("https://www.flipkart.com/search?q=laptop&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off")
#print(driver.page_source)
#print(respone.content)
soup = BeautifulSoup(respone.content, 'html.parser')
#print(soup)
products = soup.find_all('div',class_="_1AtVbE col-12-12")
print(products)
for item in products:
    print("=====================")
    Name = item.find('div', class_='_4rR01T')
    if Name is None:
        continue
    print(Name.get_text())
