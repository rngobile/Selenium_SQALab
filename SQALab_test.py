__author__ = 'Richard Ngo'

import os
from selenium import webdriver

os.
# Use Chrome
chrome_driver_path = os.getcwd() + "\chromedriver.exe"
print (chrome_driver_path)
driver = webdriver.Chrome(chrome_driver_path)

#driver = webdriver.Firefox()
driver.implicitly_wait(2)
#driver.maximize_window()

driver.get("http://www.aspire-global.net/SQALab/")

search_field = driver.find_element_by_name("q")
search_field.clear()

search_field.send_keys("phones")
search_field.submit()

products = driver.find_elements_by_xpath("//h2[@class='product-name']/a")
print ("Found "+ str(len(products)) + " products:")

for product in products:
    print (product.text)


#driver.quit()