__author__ = 'Richard Ngo'

import unittest
from selenium import webdriver

class SearchTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(2)
        #self.driver.maximize_window()

        self.driver.get("http://www.aspire-global.net/SQALab/")

    def test_search_by_category(self):
        self.search_field = self.driver.find_element_by_name("q")
        self.search_field.clear()

        self.search_field.send_keys("phones")
        self.search_field.submit()

        products = self.driver.find_elements_by_xpath("//h2[@class='product-name']/a")
        #print ("Found "+ str(len(products)) + " products:")

        for product in products:
            print (product.text)

    def test_search_by_name(self):
       self.search_field = self.driver.find_element_by_name("q")
       self.search_field.clear()
       self.search_field.send_keys("salt shaker")
       self.search_field.submit()

       product=""
       products = self.driver.find_elements_by_xpath("//h2[@class='product-name']/a")
       print("\nFound " + str(len(products)) + " Salt Shaker Products:")
       for product in products:
           print (product.text)

       self.assertEqual(1, len(products))

    def tearDown(self):
        self.driver.quit()


print(__name__)

if __name__ == '__main__':
    unittest.main()