import requests
from bs4 import BeautifulSoup
import pandas as pd
import openpyxl

with open('image_links.txt', 'w') as f:
  pass


book_dict = {
  'name': [],
  'price': [],
  'category': [],
  'stars': [],
  'upc': [],
  'availability': [],
  'in_stock': [],
  'image_link': []
}

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 Safari/537.36'}

number_dict = {'One': '1', 'Two': '2', 'Three': '3', 'Four': '4', 'Five': '5'}


url='https://books.toscrape.com/'
response=requests.get(url, headers=headers)
page_html= response.text
soup=BeautifulSoup(page_html,'html.parser')

page_count_string = soup.find('li', class_='current').text

print('page_count_string: {}'.format(page_count_string))

page_count = int(page_count_string.strip().split(' ')[-1])

print(page_count)

for page_no in range(1, page_count+1):
  print(f'page --> {page_no}')
  page_url=f'https://books.toscrape.com/catalogue/page-{page_no}.html'
  response = requests.get(page_url,headers=headers)
  page_html = response.text
  soup = BeautifulSoup(page_html, 'html.parser')
  books = soup.find_all('article', class_='product_pod')
  # print(len(books))

  for book in books:
    book_url = 'https://books.toscrape.com/catalogue/' + book.find('a')['href']
    # print(book_url)

    response = requests.get(book_url, headers=headers)
    response.encoding = 'utf8'
    soup = BeautifulSoup(response.text, 'html.parser')

    name = soup.find('div', class_='product_main').h1.text
    book_dict['name'].append(name)

    price = soup.find('div', class_='product_main').p.text
    book_dict['price'].append(price)

    ul_container = soup.find('ul', class_='breadcrumb')

    li_items = ul_container.find_all('li')

    print('\nli_items: {}'.format(li_items))

    for l in li_items:
      print(l.text)

    # print('======')
    # print(li_items[2].text)

    category = li_items[2].a.text
    book_dict['category'].append(category)
    # print('\ncategory: {}'.format(category))

    star_p_element = soup.find('p', class_='star-rating')
    print('star_p_element: {}'.format(star_p_element['class']))

    star_class_name_list = star_p_element['class']
    star_string = star_class_name_list[1]

    # print('star_class_name_list: {}'.format(star_class_name_list))
    # print('start_string: {}'.format(star_string))

    stars = number_dict[star_string]
    book_dict['stars'].append(stars)

    upc_th = soup.find('th', string='UPC')
    upc = upc_th.find_next_sibling().text
    book_dict['upc'].append(upc)

    availability_th = soup.find('th', string='Availability')
    availability = availability_th.find_next_sibling().text
    book_dict['availability'].append(availability)

    in_stock = availability.split('(')[1].split(' ')[0]
    book_dict['in_stock'].append(in_stock)

    image_link = 'https://books.toscrape.com/' + soup.find('div', class_='thumbnail').img['src'][6:]

    book_dict['image_link'].append(image_link)

    with open('image_links.txt', 'a') as f:
      f.write(image_link + '\n')

df = pd.DataFrame(book_dict)
df.to_excel('book.xlsx')



# page_no = 45
# while True:
#   print(f'page --> {page_no}')
#   page_url = f'https://books.toscrape.com/catalogue/page-{page_no}.html'
#   response = requests.get(page_url)
#   page_html = response.text
#   soup = BeautifulSoup(page_html, 'html.parser')
#   books = soup.find_all('article', class_='product_pod')
#   print(len(books))
#
#   next_button = soup.find('li', class_='next')
#   if next_button is None:
#     break
#   else:
#     page_no += 1
