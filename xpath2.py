from xml.sax import parse

from pandas.core.arraylike import dispatch_reduction_ufunc
from selenium import webdriver
from selenium.webdriver.common.by import By

# get the text inside element
# same with css selector --> element.text

# get values of the attributes of the element
# same with css selector --> element.get_attribute('att_name')


url='https://books.toscrape.com/'

options=webdriver.ChromeOptions()
options.add_argument('--start-maximized')
# options.add_argument('--headless')

driver=webdriver.Chrome(options=options)

driver.get(url)

list_item = driver.find_element(By.XPATH,'//li').text

print(list_item)

prices = driver.find_elements(By.XPATH,'//p[@class="price_color"]')

for price in prices:
    print(price.text)
    # print('\n')


price = driver.find_element(By.XPATH,'//p[@class="price_color"]')
print(f'first element price: {price.text}')

body = driver.find_element(By.XPATH,'//body[@id="default"]')
print(f'\nbody: {body.text}')

alert = driver.find_element(By.XPATH,'//div[@role="alert"]')
print(f'\nalert: {alert.text}')

next_button = driver.find_element(By.XPATH,'//a[text()="next"]')
print(type(next_button))
print('\n')
print(next_button.get_attribute('href'))

img_src = driver.find_element(By.XPATH,'//article[@class="product_pod"]/div/a/img').get_attribute('src')

print('\nimg_src: {}'.format(img_src))

first_book = driver.find_element(By.XPATH,'//article[@class="product_pod"]')
# first_book_div = first_book.find_element(By.XPATH,'./div').get_attribute('class')
# first_book_div

parent_of_first = first_book.find_element(By.XPATH,'./..')
print('\nparent_of_first: {}'.format(parent_of_first.text))
print('\ntag name: {}'.format(parent_of_first.tag_name))

following_sibling = parent_of_first.find_element(By.XPATH,'./following-sibling::li[1]')
print('\nfollowing_sibling: {}'.format(following_sibling.text))

third_book_name = parent_of_first.find_element(By.XPATH,'./following-sibling::li[2]')
print('\nthird_book_name: {}'.format(third_book_name.text))

# first_book = driver.find_element(By.XPATH,'//article[@class="product_pod"]')
second_book_name = following_sibling.find_element(By.XPATH,'./article/div/a/img').get_attribute('alt')
print('\nsecond_book_name: {}'.format(second_book_name))

book_name = driver.find_element(By.XPATH,'//article[@class="product_pod"]/../following-sibling::li[1]/article/div/a/img').get_attribute('alt')

print('\nbook_name: {}'.format(book_name))
