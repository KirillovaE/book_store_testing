# Shop: отображение страницы товара

# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# import time
# from selenium.webdriver.chrome.options import Options
# path_to_extension = r'C:\Users\PC64\AppData\Local\Google\Chrome\User Data\Default\Extensions\gighmmpiobklfepjocnamgkkbiglidom\4.40.0_0'
# chrome_options = Options()
# chrome_options.add_argument('load-extension=' + path_to_extension)
# driver = webdriver.Chrome(chrome_options=chrome_options)
# driver.create_options()
# time.sleep(10)
# driver.maximize_window()
# driver.implicitly_wait(5)
# first_browser_tab = driver.window_handles[0]
# driver.switch_to.window(first_browser_tab)
# driver.get("http://practice.automationtesting.in/")
# my_account = driver.find_element_by_link_text("My Account")
# my_account.click()
# login = driver.find_element_by_id("username")
# login.send_keys("12345@yandex.ru")
# password = driver.find_element_by_id("password")
# password.send_keys("QWEasdZXC!@12")
# time.sleep(5)
# login_btn = driver.find_element_by_name("login")
# login_btn.click()
# shop = driver.find_element_by_link_text("Shop")
# shop.click()
# html_5_forms_book = driver.find_element_by_css_selector("img[title ='Mastering HTML5 Forms']")
# html_5_forms_book.click()
# html_5_forms_book_title = WebDriverWait(driver,10).until(
# EC.text_to_be_present_in_element((By.CSS_SELECTOR, "h1.product_title.entry-title"), "HTML5 Forms"))
# driver.quit()

# Shop: количество товаров в категории

# from selenium import webdriver
# import time
# from selenium.webdriver.chrome.options import Options
# path_to_extension = r'C:\Users\PC64\AppData\Local\Google\Chrome\User Data\Default\Extensions\gighmmpiobklfepjocnamgkkbiglidom\4.40.0_0'
# chrome_options = Options()
# chrome_options.add_argument('load-extension=' + path_to_extension)
# driver = webdriver.Chrome(chrome_options=chrome_options)
# driver.create_options()
# time.sleep(10)
# driver.maximize_window()
# driver.implicitly_wait(5)
# first_browser_tab = driver.window_handles[0]
# driver.switch_to.window(first_browser_tab)
# driver.get("http://practice.automationtesting.in/")
# my_account = driver.find_element_by_link_text("My Account")
# my_account.click()
# login = driver.find_element_by_id("username")
# login.send_keys("12345@yandex.ru")
# password = driver.find_element_by_id("password")
# password.send_keys("QWEasdZXC!@12")
# time.sleep(5)
# login_btn = driver.find_element_by_name("login")
# login_btn.click()
# shop = driver.find_element_by_link_text("Shop")
# shop.click()
# html_tab = driver.find_element_by_link_text("HTML")
# html_tab.click()
# html_qty = driver.find_element_by_css_selector(".cat-item.cat-item-21>span")
# html_qty_text = html_qty.text
# assert html_qty_text == "(3)"
# driver.quit()

# Shop: сортировка товаров


# from selenium import webdriver
# from selenium.webdriver.support.select import Select
# import time
# from selenium.webdriver.chrome.options import Options
# path_to_extension = r'C:\Users\PC64\AppData\Local\Google\Chrome\User Data\Default\Extensions\gighmmpiobklfepjocnamgkkbiglidom\4.40.0_0'
# chrome_options = Options()
# chrome_options.add_argument('load-extension=' + path_to_extension)
# driver = webdriver.Chrome(chrome_options=chrome_options)
# driver.create_options()
# time.sleep(10)
# driver.maximize_window()
# driver.implicitly_wait(5)
# first_browser_tab = driver.window_handles[0]
# driver.switch_to.window(first_browser_tab)
# driver.get("http://practice.automationtesting.in/")
# my_account = driver.find_element_by_link_text("My Account")
# my_account.click()
# login = driver.find_element_by_id("username")
# login.send_keys("12345@yandex.ru")
# password = driver.find_element_by_id("password")
# password.send_keys("QWEasdZXC!@12")
# time.sleep(5)
# login_btn = driver.find_element_by_name("login")
# login_btn.click()
# shop = driver.find_element_by_link_text("Shop")
# shop.click()
# sorting_selector = driver.find_element_by_css_selector("select[name='orderby']")
# select = Select(sorting_selector)
# select.select_by_value("menu_order")
# sorting_selector = sorting_selector.get_attribute("value")
# if sorting_selector == "menu_order":
#     print("Выбран вариант сортировки по умолчанию")
# else:
#     print("Выбран вариант сортировки не по умолчанию")
# select.select_by_value("price")
# sorting_selector = driver.find_element_by_css_selector("select[name='orderby']")
# sorting_selector = sorting_selector.get_attribute("value")
# if sorting_selector == "price":
#     print("Выбран вариант сортировки от большего к меньшему")
# else:
#     print("Выбран другой вариант сортировки")
# driver.quit()

# Shop: отображение, скидка товара

# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# import time
# from selenium.webdriver.chrome.options import Options
# path_to_extension = r'C:\Users\PC64\AppData\Local\Google\Chrome\User Data\Default\Extensions\gighmmpiobklfepjocnamgkkbiglidom\4.40.0_0'
# chrome_options = Options()
# chrome_options.add_argument('load-extension=' + path_to_extension)
# driver = webdriver.Chrome(chrome_options=chrome_options)
# driver.create_options()
# time.sleep(10)
# driver.maximize_window()
# driver.implicitly_wait(5)
# first_browser_tab = driver.window_handles[0]
# driver.switch_to.window(first_browser_tab)
# driver.get("http://practice.automationtesting.in/")
# my_account = driver.find_element_by_link_text("My Account")
# my_account.click()
# login = driver.find_element_by_id("username")
# login.send_keys("12345@yandex.ru")
# password = driver.find_element_by_id("password")
# password.send_keys("QWEasdZXC!@12")
# time.sleep(5)
# login_btn = driver.find_element_by_name("login")
# login_btn.click()
# shop = driver.find_element_by_link_text("Shop")
# shop.click()
# android_qsg_book = driver.find_element_by_css_selector("img[title='Android Quick Start Guide']")
# android_qsg_book.click()
# old_price = driver.find_element_by_css_selector(".price>del>span")
# old_price_text = old_price.text
# assert old_price_text == "₹600.00"
# new_price = driver.find_element_by_css_selector(".price>ins>span")
# new_price_text = new_price.text
# assert new_price_text == "₹450.00"
# android_qsg_book_image = WebDriverWait(driver,10).until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, ".images")))
# android_qsg_book_image.click()
# android_qsg_book_close = WebDriverWait(driver,10).until(
#     EC.element_to_be_clickable((By.CSS_SELECTOR, ".pp_close")))
# android_qsg_book_close.click()
# driver.quit()

# Shop: проверка цены в корзине

# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# import time
# from selenium.webdriver.chrome.options import Options
# path_to_extension = r'C:\Users\PC64\AppData\Local\Google\Chrome\User Data\Default\Extensions\gighmmpiobklfepjocnamgkkbiglidom\4.40.0_0'
# chrome_options = Options()
# chrome_options.add_argument('load-extension=' + path_to_extension)
# driver = webdriver.Chrome(chrome_options=chrome_options)
# driver.create_options()
# time.sleep(10)
# driver.maximize_window()
# driver.implicitly_wait(5)
# first_browser_tab = driver.window_handles[0]
# driver.switch_to.window(first_browser_tab)
# driver.get("http://practice.automationtesting.in/")
# shop = driver.find_element_by_link_text("Shop")
# shop.click()
# html5_webapp_book_add_to_basket_btn = driver.find_element_by_css_selector("[data-product_id='182']")
# html5_webapp_book_add_to_basket_btn.click()
# time.sleep(10)
# basket_book_qty = driver.find_element_by_css_selector(".wpmenucart-contents>span.cartcontents")
# basket_book_qty_get_text = basket_book_qty.text
# assert basket_book_qty_get_text == "1 Item"
# basket_book_price = driver.find_element_by_css_selector(".wpmenucart-contents>span.amount")
# basket_book_price_get_text = basket_book_price.text
# assert basket_book_price_get_text == "₹180.00"
# basket = driver.find_element_by_css_selector(".wpmenucart-contents>i")
# basket.click()
# subtotal_price = WebDriverWait(driver,10).until(
#     EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".product-subtotal>.woocommerce-Price-amount.amount"), "₹180.00"))
# total_price = WebDriverWait(driver,10).until(
#     EC.text_to_be_present_in_element((By.CSS_SELECTOR, "td>strong>span"), "₹189.00"))
# driver.quit()

# Shop: работа в корзине

# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium import webdriver
# import time
# from selenium.webdriver.chrome.options import Options
# path_to_extension = r'C:\Users\PC64\AppData\Local\Google\Chrome\User Data\Default\Extensions\gighmmpiobklfepjocnamgkkbiglidom\4.40.0_0'
# chrome_options = Options()
# chrome_options.add_argument('load-extension=' + path_to_extension)
# driver = webdriver.Chrome(chrome_options=chrome_options)
# driver.create_options()
# time.sleep(10)
# driver.maximize_window()
# driver.implicitly_wait(5)
# first_browser_tab = driver.window_handles[0]
# driver.switch_to.window(first_browser_tab)
# driver.get("http://practice.automationtesting.in/")
# shop = driver.find_element_by_link_text("Shop")
# shop.click()
# driver.execute_script("window.scrollBy(0, 300);")
# html5_webapp_book_add_to_basket_btn = driver.find_element_by_css_selector("[data-product_id='182']")
# html5_webapp_book_add_to_basket_btn.click()
# time.sleep(5)
# js_data_book_add_to_basket_btn = driver.find_element_by_css_selector("[data-product_id='180']")
# js_data_book_add_to_basket_btn.click()
# basket = driver.find_element_by_css_selector(".wpmenucart-contents>i")
# basket.click()
# time.sleep(5)
# html5_webapp_book_remove_btn = driver.find_element_by_css_selector("td.product-remove>[data-product_id='182']")
# html5_webapp_book_remove_btn.click()
# undo_btn = driver.find_element_by_css_selector(".woocommerce-message>a")
# undo_btn.click()
# js_data_book_qty = driver.find_element_by_css_selector(".quantity>[name ='cart[045117b0e0a11a242b9765e79cbf113f][qty]']").clear()
# # tr.cart_item:nth-child(2)>.product-quantity>div input
# js_data_book_qty = driver.find_element_by_css_selector(".quantity>[name ='cart[045117b0e0a11a242b9765e79cbf113f][qty]']")
# js_data_book_qty.send_keys("3")
# update_basket_btn = driver.find_element_by_css_selector("input.button:nth-child(2)")
# update_basket_btn.click()
# time.sleep(5)
# js_data_book_new_qty = driver.find_element_by_css_selector("[name ='cart[045117b0e0a11a242b9765e79cbf113f][qty]']")
# js_data_book_new_qty_check = js_data_book_new_qty.get_attribute("value")
# assert js_data_book_new_qty_check == "3"
# time.sleep(5)
# apply_coupon_btn = driver.find_element_by_css_selector("div.coupon>input.button")
# apply_coupon_btn.click()
# coupon_message = WebDriverWait(driver,10).until(
#     EC.text_to_be_present_in_element((By.CSS_SELECTOR, "ul.woocommerce-error>li"), "Please enter a coupon code."))
# driver.quit()



# Shop: покупка товара

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
shop = driver.find_element_by_link_text("Shop")
shop.click()
driver.execute_script("window.scrollBy(0, 300);")
html5_webapp_book_add_to_basket_btn = driver.find_element_by_css_selector("[data-product_id='182']")
html5_webapp_book_add_to_basket_btn.click()
time.sleep(5)
basket = driver.find_element_by_css_selector(".wpmenucart-contents>i")
basket.click()
proceed_to_checkout_btn = WebDriverWait(driver,20).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR,".wc-proceed-to-checkout>a")))
proceed_to_checkout_btn.click()
first_name = driver.find_element_by_id("billing_first_name")
first_name = WebDriverWait(driver,20).until(
    EC.visibility_of_element_located((By.ID, "billing_first_name")))
first_name.send_keys("fff")
last_name = driver.find_element_by_id("billing_last_name")
last_name.send_keys("nnn")
email_address = driver.find_element_by_id("billing_email")
email_address.send_keys("abc@yandex.ru")
phone = driver.find_element_by_id("billing_phone")
phone.send_keys("+7123456789")
time.sleep(5)
country_selector = driver.find_element_by_id("s2id_billing_country")
country_selector.click()
country_name = WebDriverWait(driver,20).until(
    EC.element_to_be_clickable((By.XPATH,"//input[@class='select2-input select2-focused']")))
country_name.click()
country_name.send_keys("Montenegro")
country = driver.find_element_by_id("select2-results-1")
country.click()
address = driver.find_element_by_css_selector("#billing_address_1:nth-child(2)")
address.send_keys("abc")
city = driver.find_element_by_css_selector("#billing_city:nth-child(2)")
city.send_keys("def")
state = driver.find_element_by_css_selector("#billing_state:nth-child(2)")
state.send_keys("fgh")
zip = driver.find_element_by_css_selector("#billing_postcode:nth-child(2)")
zip.send_keys("12345")
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(5)
check_payments = driver.find_element_by_id("payment_method_cheque")
check_payments.click()
place_order = driver.find_element_by_id("place_order")
place_order.click()
window_text = WebDriverWait(driver,10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-thankyou-order-received"),"Thank you. Your order has been received."))
payment_method_text = WebDriverWait(driver,10).until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "tfoot>tr:nth-child(3)>td"), "Check Payments"))
driver.quit()





