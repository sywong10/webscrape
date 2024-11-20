from selenium import webdriver
from selenium.webdriver.common.by import By

url='https://books.toscrape.com/'

options=webdriver.ChromeOptions()
options.add_argument('--headless')

driver=webdriver.Chrome(options=options)

driver.get(url)
list_items = driver.find_elements(By.CSS_SELECTOR, 'li')
print(list_items)
print(len(list_items))

list_item = driver.find_element(By.CSS_SELECTOR, 'li').text
print(list_item)

prices = driver.find_elements(By.CSS_SELECTOR, 'p.price_color')

for price in prices:
  print(price.text)


price=driver.find_element(By.CSS_SELECTOR, 'p.price_color').text

# this returns first element
print('\n{}'.format(price))


body = driver.find_element(By.CSS_SELECTOR, 'body#default').text
print('\nbody: {}'.format(body))

body2_=driver.find_element(By.ID, 'default').text
print('\nbody2_: {}'.format(body2_))

alert=driver.find_element(By.CSS_SELECTOR, 'div[role="alert"]')
print('\nalert: {}'.format(alert.text))


image_src=driver.find_element(By.CSS_SELECTOR, 'article.product_pod div a img').get_attribute('src')
print('\nimage_src: {}'.format(image_src))


the_first_book = driver.find_element(By.CSS_SELECTOR, 'article.product_pod')
print(the_first_book.text)

warning_div_attribute = driver.find_element(By.CSS_SELECTOR, 'div.alert-warning').get_attribute('role')
print('\nwarning_div_attribute: {}'.format(warning_div_attribute))

name_of_first_element_from_alt_attribute = driver.find_element(By.CSS_SELECTOR, 'article.product_pod img').get_attribute('alt')
print('\nname_of_first_element_from_alt_attribute: {}'.format(name_of_first_element_from_alt_attribute))
