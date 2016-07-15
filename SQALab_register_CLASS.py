__author__ = 'Richard Ngo'

from selenium import webdriver
from time import gmtime, strftime
import unittest

class RegisterTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(5)

        url = 'http://www.aspire-global.net/SQALab'

        cls.driver.get(url)

    def test_register_user(self):
        user_name = "User_" + strftime("%Y%m%d%H%M%S", gmtime())

        v_firstName = 'Test'
        v_middleName = ''
        v_lastName = user_name
        v_email = user_name + "@example.com"
        v_password = 'tester'

        self.assertEquals("Madison Island", self.driver.title)

        #self.driver.find_element_by_link_text('ACCOUNT').click()
        self.driver.find_element_by_xpath("//a[@data-target-element='#header-account']").click()
        self.driver.find_element_by_xpath("//a[@title='Register']").click()
        #self.driver.find_element_by_link_text('Register').click()

        register_firstName = self.driver.find_element_by_name('firstname')
        register_lastName = self.driver.find_element_by_name('lastname')
        register_email = self.driver.find_element_by_name('email')
        register_password = self.driver.find_element_by_name('password')
        register_confirm = self.driver.find_element_by_name('confirmation')
        register_news_letter_subscription = self.driver.find_element_by_id("is_subscribed")
        register_submit = self.driver.find_element_by_xpath("//button[@title='Register']")

        self.assertTrue(register_firstName.is_enabled() and register_lastName.is_enabled() and register_email.is_enabled()
                        and register_password.is_enabled() and register_confirm.is_enabled() and register_submit.is_enabled()
        )

        register_firstName.send_keys(v_firstName)
        register_lastName.send_keys(v_lastName)
        register_email.send_keys(v_email)
        register_password.send_keys(v_password)
        register_confirm.send_keys(v_password)
        register_news_letter_subscription.click()
        register_submit.click()
        self.driver.implicitly_wait(60)
        self.driver.save_screenshot('C:\Workspace\SQALab\submit_error.jpg')
        #self.assertEqual("Hello, Test " + user_name + "!", self.driver.find_element_by_css_selector("p.hello > strong".text))
        self.assertTrue(self.driver.find_element_by_link_text("Thank you for registering with Madison Island.").is_displayed())
        self.driver.find_element_by_link_text("ACCOUNT").click()
        self.assertTrue(self.driver.find_element_by_link_text("Log Out").is_displayed())
        self.driver.find_element_by_link_text("Log Out").click()


        print('~fin.')

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

if __name__ == '__main__':
    unittest.main()