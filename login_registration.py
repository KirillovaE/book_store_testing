# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("http://practice.automationtesting.in/")
# my_account = driver.find_element_by_link_text("My Account")
# my_account.click()
# email_address = driver.find_element_by_id("reg_email")
# email_address.send_keys("12345@yandex.ru")
# password = driver.find_element_by_id("reg_password")
# password.send_keys("QWEasdZXC!@12")
# time.sleep(5)
# register_btn = driver.find_element_by_xpath("//input[@name='register']")
# register_btn.click()
# driver.quit()



import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
my_account = driver.find_element_by_link_text("My Account")
my_account.click()
login = driver.find_element_by_id("username")
login.send_keys("12345@yandex.ru")
password = driver.find_element_by_id("password")
password.send_keys("QWEasdZXC!@12")
time.sleep(5)
login_btn = driver.find_element_by_name("login")
login_btn.click()
logout = WebDriverWait(driver,20).until(
EC.visibility_of_element_located((By.LINK_TEXT, "Logout")))
# logout = driver.find_element_by_link_text("logout")
logout_get_text = logout.text
assert logout_get_text == "Logout"
logout.click()
driver.quit()



