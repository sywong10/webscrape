import requests
from bs4 import BeautifulSoup
import pandas as pd
import openpyxl

laptop_dict ={
  'name': [],
  'price': [],
  'shipping': [],
  'link': []
}

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Safari/605.1.15'}


page_no=1
while True:
  print('*****************')
  print(f'page no --> {page_no}')
  print('*****************')
  url = f'https://www.ebay.com/sch/i.html?_from=R40&_sacat=0&RAM%2520Size=32%2520GB&Storage%2520Type=SSD%2520%2528Solid%2520State%2520Drive%2529&rt=nc&Hard%2520Drive%2520Capacity=1%2520TB&_oaa=1&_dcat=177&_nkw=laptop&_pgn={page_no}'
  print('{}\n'.format(url))
  # page

  response = requests.get(url, headers=headers)
  print(response.status_code)

  if response.status_code != 200:
    continue

  page_html = response.text
  soup=BeautifulSoup(page_html,'html.parser')
  print(soup.title)
  container=soup.find('div', attrs={'id': 'srp-river-results'})
  laptops=container.ul.find_all('div', class_='s-item__info')
  for laptop in laptops:
    # name, price, shipping, link

    if laptop.find('span', attrs={'role': 'heading'}).text is not None:
      name = laptop.find('span', attrs={'role': 'heading'}).text
      laptop_dict['name'].append(name)
      print(name)
    else:
      name = 'No Info'
      laptop_dict['name'].append(name)
      print(name)

    if laptop.find('span', class_='s-item__price').text is not None:
      price = laptop.find('span', class_='s-item__price').text
      laptop_dict['price'].append(price)
      print(price)
    else:
      price = 'No Info'
      laptop_dict['price'].append(price)
      print(price)


    # shipping = laptop.find('span', class_='s-item__logisticsCost').text
    # shipping2 = laptop.find('span', class_='s-item__shipping').text

    if laptop.find('span', class_='s-item__logisticsCost') is not None:
      shipping = laptop.find('span', class_='s-item__logisticsCost').text
      laptop_dict['shipping'].append(shipping)
      print('shipping: {}'.format(shipping))
    else:
      shipping = 'No Info'
      laptop_dict['shipping'].append(shipping)
      print('shipping: {}'.format(shipping))

    if laptop.find('a', class_='s-item__link') is not None:
      link = laptop.find('a', class_='s-item__link')['href']
      laptop_dict['link'].append(link)
      print('link: {}\n'.format(link))
    else:
      link = 'Non Info'
      laptop_dict['link'].append(link)
      # link = laptop.find('a', class_='s-item__link')['href']
      print('link: {}\n'.format(link))

  next_as_button = soup.find('button', class_='pagination__next')

  if next_as_button is not None:
    break

  page_no += 1

  print('\n\n')

df = pd.DataFrame(laptop_dict)
df.to_excel('laptops.xlsx')

