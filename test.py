import requests
from bs4 import BeautifulSoup

url ='https://books.toscrape.com/'

response = requests.get(url)

print(response)

print(response.text)

page_html=response.text

soup=BeautifulSoup(page_html,'html.parser')

# print(soup)

print(soup.prettify())


