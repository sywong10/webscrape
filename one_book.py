from importlib.util import source_hash

import requests
from bs4 import BeautifulSoup

book_url='https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'
response = requests.get(book_url)
response.encoding='utf8'

print(response.text)

print('\n\n========')

soup = BeautifulSoup(response.text, 'html.parser')

print('\nsoup: {}'.format(soup))

# will scrape:
# name, price, category, stars, upc, availability, in_stock, availability, in_stock, image_link

name = soup.find('div', class_='product_main')

print('\nsoup.find: {}\n'.format(name.h1.text))

price = soup.find('div', class_='product_main').p.text
print('\nprice: {}'.format(price))

