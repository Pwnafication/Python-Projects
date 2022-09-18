import requests
import pandas as pd
from bs4 import BeautifulSoup
from tabulate import tabulate

url = "https://pokemondb.net/move/all"
page = requests.get(url)

soup = BeautifulSoup(page.text, features="html.parser")

table1 = soup.find('table', {'id': 'moves'})

headers = []

for XX in table1.find_all('th'):
    title = XX.text
    headers.append(title)

mydata = pd.DataFrame(columns=headers)

for XX in table1.find_all('tr')[1:]:
    row_data = XX.find_all('td')
    row = [YY.text for YY in row_data]
    length = len(mydata)
    mydata.loc[length] = row

tendata = mydata.head(10)

print(tabulate(tendata, headers = 'keys', tablefmt = 'psql'))