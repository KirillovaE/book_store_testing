from selenium import webdriver
from selenium.webdriver.support.select import Select
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
driver.execute_script("window.scrollBy(0, 600);")
Selenium_Ruby = driver.find_element_by_css_selector("#text-22-sub_row_1-0-2-0-0 h3")
Selenium_Ruby.click()
time.sleep(3)
rewiews = driver.find_element_by_css_selector(".reviews_tab>a")
rewiews.click()
time.sleep(5)
stars = driver.find_element_by_css_selector(".stars > span :nth-child(5)")
stars.click()
your_rewiew = driver.find_element_by_id("comment")
your_rewiew.send_keys("Nice book!")
name = driver.find_element_by_id("author")
name.send_keys("aaa")
email = driver.find_element_by_id("email")
email.send_keys("aaa@yandex.ru")
submit_btn = driver.find_element_by_id("submit")
submit_btn.click()
driver.quit()
