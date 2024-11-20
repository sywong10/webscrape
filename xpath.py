from selenium import webdriver
from selenium.webdriver.common.by import By

from src.selenium_basics import driver

url='https://books.toscrape.com/'

options=webdriver.ChromeOptions()
options.add_argument('--start-maximized')
# options.add_argument('--headless')

driver=webdriver.Chrome(options=options)

driver.get(url)

list_items=driver.find_elements(By.XPATH,'//li')
print(len(list_items))

for item in list_items:
  print(item.text)


url='https://books.toscrape.com/'
driver.get(url)

list_item = driver.find_element(By.XPATH,'//li').text

print(list_item)



