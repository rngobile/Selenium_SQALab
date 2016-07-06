__author__ = 'Richard Ngo'

from selenium import webdriver

driver = webdriver.Firefox()
driver.implicitly_wait(2)

url = 'http://newtours.demoaut.com'
v_firstName = 'Ninja'
v_lastName = 'Turtles'
v_phone = '555-555-5555'
v_email = 'ninja.turtles@shellshock.com'
v_address = '123456 Sewer Lane'
v_city = 'Sewer'
v_state = 'New York'
v_postCode = '55555'
v_userName = 'ninja.turtles'
v_password = 'password'

driver.get(url)

register = driver.find_element_by_link_text('REGISTER')
register.click()

firstName = driver.find_element_by_name('firstName')
firstName.send_keys(v_firstName)

lastName = driver.find_element_by_name('lastName')
lastName.send_keys(v_lastName)

phone = driver.find_element_by_name('phone')
phone.send_keys(v_phone)

email = driver.find_element_by_id('userName')
email.send_keys(v_email)

address = driver.find_element_by_name('address1')
address.send_keys(v_address)

city = driver.find_element_by_name('city')
city.send_keys(v_city)

state = driver.find_element_by_name('state')
state.send_keys(v_state)

postalCode = driver.find_element_by_name('postalCode')
postalCode.send_keys(v_postCode)

userName = driver.find_element_by_id('email')
userName.send_keys(v_userName)

password = driver.find_element_by_name('password')
password.send_keys(v_password)

verifyPass = driver.find_element_by_name('confirmPassword')
verifyPass.send_keys(v_password)

submit = driver.find_element_by_name('register')
submit.click()

signIn = driver.find_element_by_link_text('sign-in')
signIn.click()

signInUser = driver.find_element_by_name('userName')
signInUser.send_keys(v_userName)

signInPass = driver.find_element_by_name('password')
signInPass.send_keys(v_password)

login = driver.find_element_by_name('login')
login.click()

profile = driver.find_element_by_link_text('PROFILE')
profile.click()

profileFirstName = driver.find_element_by_name('firstName')
profileFirstName.send_keys(v_firstName)

profileLastName = driver.find_element_by_name('lastName')
profileLastName.send_keys(v_lastName)

profilePhone = driver.find_element_by_name('phone')
profilePhone.send_keys(v_phone)

profileEmail = driver.find_element_by_name('email')
profileEmail.send_keys(v_email)

profileAddress = driver.find_element_by_name('address1')
profileAddress.send_keys(v_address)

profileCity = driver.find_element_by_name('city')
profileCity.send_keys(v_city)

profileState = driver.find_element_by_name('state')
profileState.send_keys(v_state)

profilePostal = driver.find_element_by_name('postalCode')
profilePostal.send_keys(v_postCode)

profileCountry = driver.find_element_by_xpath("//select[@name='country']/option[@value='215']")
profileCountry.click()

