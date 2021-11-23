import requests
from bs4 import BeautifulSoup
import pandas as pd
from xlsxwriter import Workbook
from time import sleep

cars = []
headers = ['Модель', 'Год', 'Двигатель', 'Диллер', 'Цена в $', 'Цена €', 'Ссылка']
for p in range(1, 14):
  url = f'https://salon.av.by/adverts/?iPageNo={p}&sort=0'
  response = requests.get(url)
  response.text
  sleep(5)
  soup = BeautifulSoup(response.text, 'lxml')
  items = soup.find_all('li', class_='card_list_item')
  for item in items:
    try:
      model = item.find('a', class_='model').get_text()
    except:
      model = '—'
    try:
      year = item.find('div', class_='year').get_text()
    except:
      year = '—'
    try:
      engine = item.find('ul', class_='grade').find('a').get_text()
    except:
      engine = '—'
    try:
      dealer = item.find('a', class_='dealer').get_text()
    except:
      dealer = '—'
    try:
      usd_price = item.find('span', class_='i-p currency_USD').get_text()
    except:
      usd_price = '—'
    try:
      euro_price = item.find('span', class_='i-p currency_EUR').get_text()
    except:
      euro_price = '—'
    try:
      link = url+item.find('a', class_='full_link title').get('href')
    except:
      link = '—'

    cars.append([model, year, engine, dealer, usd_price, euro_price, link])
    print(cars)

table = pd.DataFrame(data=cars, columns=headers)
writer = pd.ExcelWriter('cars.xlsx', engine='xlsxwriter')
table.to_excel(writer, index=False)
writer.save()





















