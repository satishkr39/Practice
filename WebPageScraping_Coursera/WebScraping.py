import requests as req
from bs4 import BeautifulSoup
import shutil

r = req.get("https://en.wikipedia.org/wiki/India")
print(r.content[:2000])

soup = BeautifulSoup(r.content,'html.parser')
#print(soup.prettify())

title = soup.h1
print(title)

#find the imags tag in complete page
print(soup.img)

#to find all the tables
tables = soup.find_all("table")
print("Length of tables: ",len(tables))

#To access the table 0
print("======== Table 0 tag details :::: ",tables[0])

#to access attribute of table -- here attribute style of table 0
print("Tables 0 style :::: ",tables[0]["style"])

#to find the li tage items
lists = soup.find_all("li")
print("===============Length of li tag ::: ",len(lists))

#To get the children of element list
childs = list(lists[3].children)
print("======= Length of Childres of 3rd list item ::: ",len(childs))
print("=== == Printing the childs :: ",childs)


#Searching the elements by Class and Identifier
#to find the links
links = soup.find_all("a")
print("===== Length of links ::",len(links))

#to get first 5 links
print("===================FIRST 5 LINKS ==============")
print(links[0:5])

#To filter the link tag using some attribue (here class)
print("============= Attribute Filter ============")
attribute_filter = {"class":"mw-jump-link"}
print(soup.find_all('a', attribute_filter)) #this will find all a tags having class as mw-jump-link

#attribue filter is a dictionary having key value pair
print("==============Using attribue filter 1 =======")
attribute_filter_1 = {"class":"mw-jump-link", "href":"#searchInput"}
print(soup.find_all('a', attribute_filter_1))


#if we don't want to specify tag then we shoul type None
print("=========== TAG None Example ========")
print(soup.find_all(None, attribute_filter))

#Find element by ID
print("============= FInding by ID example ============")
print(soup.find_all(None, attrs={"id":"firstHeading"}))

#Tips to Use Developer tools on browser
'''
Right click on source page
click on inspect element
We can copy the xpath, css selector, and others by doing right click on code and then 
navigate to copy and copy the desired thing required. it can be used to find out the 
repective tags and value using python
'''

#Scrape pictures from the website using CSS selector
print("=============== Accessing the Image ==================")
selector = "#mw-content-text > div.mw-parser-output > table.infobox.geography.vcard > tbody > tr:nth-child(2) > td > div > div:nth-child(1) > div:nth-child(1) > a > img"
images = soup.select(selector)
print(images[0]["src"])


#To get first 3 thumnail image
print("================ To GET First 3 thumnail Image ===========")
selector_1 = ".thumbimage"
print(soup.select(selector_1, limit=3)) #to get first 3 only


#Send POST, PUT, PATCH using Headers\
print("============== PATCH COMMAND ==============")
r = req.patch('https://httpbin.org/patch', data={'key': 'value'})
# check status code for response recieved
# success code - 200
print(r)
# print content of request
print(r.content)