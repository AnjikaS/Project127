from bs4 import BeautifulSoup as bs
import bs4
import selenium
import requests
import csv
import time
import pandas as pd

start_url = "https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars"
page = requests.get(start_url)
time.sleep(10)
print(page)

soup = bs(page.text,'html.parser')
star_table = soup.find('table')

temp_list= []
table_rows = star_table.find_all('tr')


for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]
    temp_list.append("row")

#headers = ["name","distance","mass","radius","luminosity"]
Star_names = []
Distance = []
Mass = []
Radius = []
Lum = []

for i in range(1,len(temp_list)):
    Star_names.append(temp_list[i][1])
    Distance.append(temp_list[i][2])
    Mass.append(temp_list[i][1])
    Radius.append(temp_list[i][2])
    Lum.append(temp_list[i][1])

df2 = pd.DataFrame(list(zip(Star_names,Distance,Mass,Radius,Lum)),columns=['Star_name','Distance','Mass','Radius','Luminosity'])

print(df2)
df2.to_csv('start.csv')