import urllib.request
from bs4 import BeautifulSoup
import pandas as pd

# site = 'https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India'
site = input('Please paste the website url....')
page = urllib.request.urlopen(site)

soup = BeautifulSoup(page, "html.parser")

# print(soup.prettify())
# print(soup.title.string)
all_tables = soup.find_all('table', class_='wikitable sortable plainrowheaders')
right_table = soup.find('table' , { 'class' : 'wikitable sortable plainrowheaders' })
# print(all_tables)
#Generate lists
A=[]
B=[]
C=[]
D=[]
E=[]
F=[]
G=[]

for row in right_table.findAll("tr"):
    cells = row.findAll('td')
    states=row.findAll('th') #To store second column data
    if len(cells)==6: #Only extract table body not heading
        A.append(cells[0].find(text=True))
        B.append(states[0].find(text=True))
        C.append(cells[1].find(text=True))
        D.append(cells[2].find(text=True))
        E.append(cells[3].find(text=True))
        F.append(cells[4].find(text=True))
        G.append(cells[5].find(text=True))

#use pandas to convert list to data frame
df=pd.DataFrame(A,columns=['Number'])
df['State/UT']=B
df['Admin_Capital']=C
df['Legislative_Capital']=D
df['Judiciary_Capital']=E
df['Year_Capital']=F
df['Former_Capital']=G

# print(A)
print(df)