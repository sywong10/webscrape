from selenium import webdriver
from selenium.webdriver.common.by import By

def login(the_driver):
  login_button = the_driver.find_element(By.XPATH, '//a[text()="Login"]')
  login_button.click()

  username_input = the_driver.find_element(By.ID, 'username')
  username_input.send_keys('myusername')

  password_input = the_driver.find_element(By.ID, 'password')
  password_input.send_keys('123456')

  log_me_in = the_driver.find_element(By.CSS_SELECTOR, 'input[value="Login"]')
  log_me_in.click()


url = 'https://quotes.toscrape.com/js/'

options = webdriver.ChromeOptions()
options.add_argument('--start-maximized')
options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=options)
driver.get(url)

login(driver)

