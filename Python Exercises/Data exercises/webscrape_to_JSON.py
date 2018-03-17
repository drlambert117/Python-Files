#Imports
import urllib.request
from bs4 import BeautifulSoup
import json
import pandas as pd

#Catches user's url input and opens it
# site = input('Please enter the url for the page you would like the data for...')
test_data = 'http://econpy.pythonanywhere.com/ex/001.html'
page = urllib.request.urlopen(test_data)

#Import page into BeautifulSoup
soup = BeautifulSoup(page, "html.parser")

#Use BeautifulSoup to search dataset for div tags
info = soup.find_all('div', title = 'buyer-info')

#Generate lists
A=[]
B=[]

#for statement that sorts data by tags and appends them to the generated lists
for row in info:
    buyer_names = row.find_all('div', title = 'buyer-name')
    item_price = row.find_all('span', class_ =  'item-price')
    A.append(buyer_names[0].find(text = True))
    B.append(item_price[0].find(text = True))

json_data =  json.dumps([{'Buyer Name': buyer_name, 'Item Price': item_price} for buyer_name, item_price in zip(A, B)])

with open('output.webscrape_to_JSON.json', 'w') as outfile:
    json.dump(json_data, outfile)

#use pandas to convert list to data frame
df=pd.DataFrame()
df['Buyer Name']=A
df['Item Price']=B

#Display dataframe
print(df)