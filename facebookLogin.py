from selenium import webdriver
from getpass import getpass

usr = input('Enter your username or email : ')
pas = getpass('Enter your Password :')

driver = webdriver.Chrome()
driver.get('https://www.facebook.com/')

username = driver.find_element_by_id('email')
username.send_keys(usr)

pwd = driver.find_element_by_id('pass')
pwd.send_keys(pas)

login_button = driver.find_element_by_id('loginbutton')
login_button.submit()
