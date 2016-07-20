import xlrd, unittest
from ddt import ddt, data, unpack
from time import gmtime, strftime
from selenium import webdriver
from xlrd import open_workbook,cellname

class SearchExcelDDT(unittest.TestCase):
    def setUp(self):
        # create a new Firefox session
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()

        # navigate to the application home page
        print ("get main 1st")
        self.driver.get("http://aspire-global.net/SQALab/customer/account/create/")


    def test_register_new_user(self):
        driver = self.driver
        #get/build data values
        user_name = "user_" + strftime("%Y%m%d%H%M%S", gmtime())
        book = open_workbook('TestData.xlsx')
        sheet = book.sheet_by_index(0)
        print (sheet.name)
        print (sheet.ncols)
        for row_idx in range(sheet.nrows):
            #create_account_button.click()

            # check title
            self.assertEqual("Create New Customer Account", driver.title)

            # get all the fields from Create an Account form
            first_name = driver.find_element_by_id("firstname")
            last_name = driver.find_element_by_id("lastname")
            email_address = driver.find_element_by_id("email_address")
            password = driver.find_element_by_id("password")
            confirm_password = driver.find_element_by_id("confirmation")
            news_letter_subscription = driver.find_element_by_id("is_subscribed")
            submit_button = driver.\
                find_element_by_xpath("//button[@title='Register']")

            # check maxlength of first name and last name textbox
            self.assertEqual("255", first_name.get_attribute("maxlength"))
            self.assertEqual("255", last_name.get_attribute("maxlength"))

            # check all fields are enabled
            self.assertTrue(first_name.is_enabled() and last_name.is_enabled() and
                            email_address.is_enabled() and
                            news_letter_subscription.is_enabled() and
                            password.is_enabled() and confirm_password.is_enabled()
                            and submit_button.is_enabled())

            # check Sign Up for Newsletter is unchecked
            #self.assertFalse(news_letter_subscription.is_selected())
            print(sheet.row(row_idx))
            firstname1 = sheet.cell(row_idx,0).value
            lastname1 = sheet.cell(row_idx,1).value
            emailaddress1 = sheet.cell(row_idx,2).value
            passwordtext1 = sheet.cell(row_idx,3).value
            confirmpasswordtext1 = sheet.cell(row_idx,4).value
            subscription1 = sheet.cell(row_idx,5).value

            # fill out all the fields
            first_name.send_keys(firstname1)
            last_name.send_keys(lastname1)
            news_letter_subscription.click()
            email_address.send_keys(emailaddress1)
            password.send_keys(passwordtext1)
            confirm_password.send_keys(confirmpasswordtext1)
            #if  subscription yes, click the box
            #if subscription == "Y":
            #    news_letter_subscription.click()

             # click Submit button to submit the form
            submit_button.click()

            driver.get ("http://aspire-global.net/SQALab/customer/account/create/")
    def tearDown(self):
        # close the browser window
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
