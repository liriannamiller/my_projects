import requests
from bs4 import BeautifulSoup
from time import sleep
import pandas as pd
from xlsxwriter import Workbook
films = []
headers = ['Оригинальный заголовок', 'Заголовок', 'Страна', 'Рейтинг', 'Ссылка']
for p in range(1, 6):
    url = f"https://www.kinopoisk.ru/lists/top250/?page={p}&tab=all"
    r = requests.get(url)
    r.text
    sleep(3)
    soup = BeautifulSoup(r.text, 'lxml')
    items = soup.find_all('div', class_='desktop-rating-selection-film-item')
    for item in items:
        title = item.find('a', class_='selection-film-item-meta__link').find('p', class_='selection-film-item-meta__original-name').text
        rus_title = item.find('a', class_='selection-film-item-meta__link').find('p', class_='selection-film-item-meta__name').text
        country = item.find('a', class_='selection-film-item-meta__link').find('span', class_='selection-film-item-meta__meta-additional-item').text
        rating = item.find('span', class_='rating__value rating__value_positive').text
        link = url+item.find('a', class_='selection-film-item-meta__link').get('href')

        films.append([title, rus_title, country, rating, link])

df = pd.DataFrame(data=films, columns=headers)
writer = pd.ExcelWriter('films.xlsx', engine='xlsxwriter')
df.to_excel(writer, index=False)
writer.save()


























