import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://www.flipkart.com/search?q=mi%20mobiles&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
r = requests.get(url)
c = BeautifulSoup(r.content, 'html.parser')

# Initialize empty lists to store data
names = []
prices = []
ratings = []

# Extract data from the page
name_elements = c.find_all('div', {'class': '_4rR01T'})
price_elements = c.find_all('div', {'class': '_30jeq3'})
rating_elements = c.find_all('div', {'class': '_3LWZlK'})

# Loop through the elements and extract text data
for name_element, price_element, rating_element in zip(name_elements, price_elements, rating_elements):
    names.append(name_element.text)
    prices.append(price_element.text)
    ratings.append(rating_element.text)

# Create a DataFrame
data = {
    'Name': names,
    'Price': prices,
    'Rating': ratings
}

df = pd.DataFrame(data)

# Print the DataFrame
print(df)
