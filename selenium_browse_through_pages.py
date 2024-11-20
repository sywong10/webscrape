from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium_login import login
# from selenium_scrape import scrape_page
import pandas as pd
import openpyxl

quote_dict = { 'quote': [], 'author': [], 'tags': [] }

url = 'https://quotes.toscrape.com/js/'

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_experimental_option('detach', True)

driver=webdriver.Chrome(options=options)


def scrape_page(the_driver, the_dict):
  quotes = the_driver.find_elements(By.CLASS_NAME, 'quote')


  # quotes, author, tags

  for element in quotes:
    print(type(element))
    quote = element.find_element(By.CSS_SELECTOR, 'span.text').text
    if quote:
      the_dict['quote'].append(quote)

    author = element.find_element(By.CSS_SELECTOR, 'small.author').text
    the_dict['author'].append(author)
    print(quote)
    print(author)

    tag_container = element.find_element(By.CLASS_NAME, 'tags')
    a_tags = tag_container.find_elements(By.CSS_SELECTOR, 'a')

    print('\na_tags: {}'.format(a_tags))

    tags = ''

    for i, a_tag in enumerate(a_tags):
      if i == len(a_tags) - 1:
        tag = a_tag.text
      else:
        tag = a_tag.text + ', '

      tags += tag

    print('\tags: {}'.format(tags))
    the_dict['tags'].append(tags)
    print('=========')


driver.get(url)
login(driver)

while True:
  scrape_page(driver, quote_dict)
  try:
    next_button = driver.find_element(By.CSS_SELECTOR, 'li.next a')
    next_button.click()
  except:
    break



scrape_page(driver, quote_dict)


df = pd.DataFrame(quote_dict)
df.to_excel('quotes.xlsx')
