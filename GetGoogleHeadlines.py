import requests
from bs4 import BeautifulSoup

page = requests.get("https://news.google.com/topstories?tab=rn&hl=en-IN&gl=IN&ceid=IN:en")
print(page.status_code)


print("--------------------")

soup = BeautifulSoup(page.content, 'html.parser')

headlines = list(soup.find_all('a',class_='DY5T1d'))

for head in headlines:
    print(head.get_text())

'''print(len(headlines))
child_headlines = list(headlines.children)[0]
print(child_headlines)'''

#print(soup.find_all('a',class_='DY5T1d'))
