__author__ = 'Richard Ngo'

import xlrd, unittest
from ddt import ddt, data, unpack
from selenium import webdriver
from xlrd import open_workbook, cellname
from time import gmtime, strftime

class RegisterTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.implicitly_wait(5)

        global url
        url = 'http://www.aspire-global.net/SQALab/customer/account/create/'

        cls.driver.get(url)

    def test_register_user(self):
        driver = self.driver
        user_name = "User_" + strftime("%Y%m%d%H%M%S", gmtime())
        book = open_workbook('userdata.xlsx')
        sheet = book.sheet_by_index(0)
        print sheet.name
        print (sheet.ncols)

        for row_idx in range(sheet.nrows):

            print(sheet.row(row_idx))
            v_firstName = sheet.cell(row_idx,0).value
            v_middleName = sheet.cell(row_idx,2).value
            v_lastName = sheet.cell(row_idx,1).value
            v_email = sheet.cell(row_idx,3).value
            v_password = sheet.cell(row_idx,4).value
            v_subscription = sheet.cell(row_idx,6).value

            self.assertEqual("Create New Customer Account", driver.title)

            register_firstName = driver.find_element_by_name('firstname')
            register_lastName = driver.find_element_by_name('lastname')
            register_email = driver.find_element_by_name('email')
            register_password = driver.find_element_by_name('password')
            register_confirm = driver.find_element_by_name('confirmation')
            register_news_letter_subscription = driver.find_element_by_id("is_subscribed")
            register_submit = driver.find_element_by_xpath("//button[@title='Register']")

            self.assertEqual("255", register_firstName.get_attribute("maxlength"))
            self.assertEqual("255", register_lastName.get_attribute("maxlength"))

            self.assertTrue(register_firstName.is_enabled() and register_lastName.is_enabled() and register_email.is_enabled()
                            and register_password.is_enabled() and register_confirm.is_enabled() and register_submit.is_enabled()

            )

            register_firstName.send_keys(v_firstName)
            register_lastName.send_keys(v_lastName)
            register_email.send_keys(v_email)
            register_password.send_keys(v_password)
            register_confirm.send_keys(v_password)
            if v_subscription.upper() == "Y":
                register_news_letter_subscription.click()
            register_submit.click()

            try:
                driver.find_element_by_css_selector("li.success-msg")
                v_success = 1
            except:
                v_success = 0

            if v_success == 1:
                driver.find_element_by_link_text("ACCOUNT").click()
                self.assertTrue(self.driver.find_element_by_link_text("Log Out").is_displayed())
                driver.find_element_by_link_text("Log Out").click()
            
            driver.get(url)

            #self.driver.implicitly_wait(60)
            #self.driver.save_screenshot('C:\Workspace\SQALab\submit_error.jpg')
            #self.assertEqual("Hello, Test " + user_name + "!", self.driver.find_element_by_css_selector("p.hello > strong".text))
            #self.assertTrue(self.driver.find_element_by_link_text("Thank you for registering with Madison Island.").is_displayed())



        print('~fin.')

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()

if __name__ == '__main__':
    unittest.main()