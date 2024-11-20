from importlib.util import source_hash
from unicodedata import category

import requests
from bs4 import BeautifulSoup

book_url='https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html'
response = requests.get(book_url)
response.encoding='utf8'

print(response.text)

print('\n\n========')

soup = BeautifulSoup(response.text, 'html.parser')

print('\nsoup: {}'.format(soup))

number_dict ={'One': '1', 'Two':'2', 'Three':'3', 'Four':'4', 'Five':'5'}

# will scrape:
# name, price, category, stars, upc, availability, in_stock, availability, in_stock, image_link

name = soup.find('div', class_='product_main')
print('\nsoup.find: {}\n'.format(name.h1.text))

price = soup.find('div', class_='product_main').p.text
print('\nprice: {}'.format(price))

ul_container = soup.find('ul', class_='breadcrumb')

li_items = ul_container.find_all('li')

print('\nli_items: {}'.format(li_items))

for l in li_items:
  print(l.text)

# print('======')
# print(li_items[2].text)

category=li_items[2].a.text
print('\ncategory: {}'.format(category))

star_p_element=soup.find('p', class_='star-rating')
print('star_p_element: {}'.format(star_p_element['class']))

star_class_name_list=star_p_element['class']
star_string = star_class_name_list[1]

print('star_class_name_list: {}'.format(star_class_name_list))
print('start_string: {}'.format(star_string))

stars=number_dict[star_string]
print('stars: {}'.format(stars))

upc_th = soup.find('th', string='UPC')
upc = upc_th.find_next_sibling().text
print('upc: {}'.format(upc))

availability_th = soup.find('th', string='Availability')
availability = availability_th.find_next_sibling().text
print('availability: {}'.format(availability))

in_stock=availability.split('(')[1].split(' ')[0]
print('in_stock: {}'.format(in_stock))

image_link= 'https://books.toscrape.com/' + soup.find('div', class_='thumbnail').img['src'][6:]
print('image_link: {}'.format(image_link))
