
# import The selenium library using 'pip3 install selenium '
from selenium import webdriver

# set the User name or Group name
name = input('Enter the name of the user or group : ')

# set the text message
msg = input('Enter the message : ')

# set the message Number
count = int(input('Enter the count : '))


# This is use for open Chrome browser
driver = webdriver.Chrome()

# This is use for open website
driver.get('https://web.whatsapp.com/')


#  This is the final key press before the start script 
input('Enter anything after scanning QR code')

# this is use for find the user title name in the browser 
user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))

# this is use for click the span tag
user.click()

# this is use for find the message box class name in the browser 
msg_box = driver.find_element_by_class_name('_13mgZ')

# start the for-in loop in count
for i in range(count):
    msg_box.send_keys(msg)
    button = driver.find_element_by_class_name('_3M-N-')
    button.click()