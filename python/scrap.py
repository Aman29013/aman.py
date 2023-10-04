import requests
from bs4 import BeautifulSoup
import pandas as pd
url="https://www.flipkart.com/search?q=mi%20mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
r=requests.get(url)
c=BeautifulSoup(r.content,'html.parser')
name=c.find_all('div',{'class':"_4rR01T"})
#print(name[0])
price=c.find_all('div',{'class':"_30jeq3 _1_WHN1"})
#print(price[0])
rating=c.find_all('div',{'class':"_3LWZlK"})
#print(rating[0])
n=[]
p=[]
r=[]
for name,price,rating in zip(name,price,rating):
    n.append(name.text)

    p.append(price.text)

    r.append(rating.text)
data={'NAME':n,'PRICE':p,'RATING':r}
#data={'NAME':n}
df=pd.DataFrame(data)
print(df)