import requests
from bs4 import BeautifulSoup
import pandas as pd
url="https://www.flipkart.com/search?q=mobiles+under+10000+rupees&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_13_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_13_na_na_na&as-pos=1&as-type=HISTORY&suggestionId=mobiles+under+10000+rupees%7CMobiles&requestId=7182c59e-a8a5-442f-b64a-525b2c18613d"
req=requests.get(url)
content=BeautifulSoup(req.content,'html.parser')
#print(content)
#name=content.find_all('div',{'class':"})
price=content.find_all('div',{"class":"_30jeq3 _16Jk6d"})
rating=content.find_all('div',{"class":"_3LWZlK"})
name=content.find_all('div',{"class":"B_NuCI"})
print(rating[0])
#print(price[0])
rt=[]
pr=[]
for i in rating:
    rt.append(i.text)
#for j in price: 
#    pr.append(j.text)
data={'RATING':rt}
df=pd.DataFrame(data)
print(df)
