import requests
from bs4 import BeautifulSoup

url="https://codewithharry.com"
r=requests.get(url)
htmlcontent=r.content
#print(htmlcontent)
soup=BeautifulSoup(htmlcontent,'html.parser')
#print(soup.prettify)                   
title=soup.title
#print(type(title.string))
paras=soup.find_all('a')
anchors=soup.find_all('a')
all_links=set()
for link in anchors:
    if(link!='#'):
       link="https://codewithharry.com"+link.get('href')
       all_links.add(link)
    print(link) 

