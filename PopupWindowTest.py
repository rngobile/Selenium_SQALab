__author__ = 'Richard'

from selenium import webdriver
import unittest
import time

class PopupWindowTest(unittest.TestCase):
    URL = "https://rawgit.com/upgundecha/learnsewithpython/master/pages/Config.html"

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get(self.URL)

    def test_window_popup(self):
        driver = self.driver

        #Save main window handle
        parent_window_id = driver.current_window_handle
        help_button = driver.find_element_by_id("helpbutton")
        help_button.click()
        driver.switch_to_window("HelpWindow")
        time.sleep(2)
        driver.close()
        driver.switch_to_window(parent_window_id)
        time.sleep(2)

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()