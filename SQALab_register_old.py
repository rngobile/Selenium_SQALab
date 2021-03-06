__author__ = 'Richard Ngo'

from selenium import webdriver
from time import gmtime, strftime
import unittest

def setup():
    driver = webdriver.Firefox()
    driver.implicitly_wait(2)

    user_name = "User_" + strftime("%Y%m%d%H%M%S", gmtime())


    url = 'http://www.aspire-global.net/SQALab'
    v_firstName = 'Test'
    v_middleName = ''
    v_lastName = user_name
    v_email = user_name + "@example.com"
    v_password = 'tester'

    driver.get(url)

def test_lookup-by-category(self):
    #driver.find_element_by_link_text('ACCOUNT').click()
    driver.find_element_by_xpath("//a[@data-target-element='#header-account']").click()
    driver.find_element_by_xpath("//a[@title='Register']").click()
    #driver.find_element_by_link_text('Register').click()

    register_firstName = driver.find_element_by_name('firstname')
    register_lastName = driver.find_element_by_name('lastname')
    register_email = driver.find_element_by_name('email')
    register_password = driver.find_element_by_name('password')
    register_confirm = driver.find_element_by_name('confirmation')
    register_news_letter_subscription = driver.find_element_by_id("is_subscribed")
    register_submit = driver.find_element_by_xpath("//button[@title='Register']")

    register_firstName.send_keys(v_firstName)
    register_lastName.send_keys(v_lastName)
    register_email.send_keys(v_email)
    register_password.send_keys(v_password)
    register_confirm.send_keys(v_password)
    register_news_letter_subscription.click()
    register_submit.click()


    driver.find_element_by_link_text("ACCOUNT").click()
    driver.find_element_by_link_text("Log Out").click()

def teardown():
    driver.close()


