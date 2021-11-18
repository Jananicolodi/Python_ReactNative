# from selenium import webdriver
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

chrome = webdriver.Chrome(ChromeDriverManager().install())
# chrome = webdriver.Chrome()
chrome.maximize_window()
# chrome.back()
chrome.get("http://faceboook.com")

element_email = chrome.find_element_by_id("email")
element_pass = chrome.find_element_by_id("pass")
element_botao = chrome.find_element_by_id("u_0_b")

element_email.send_keys("jananicolodi@hotmail.com")
element_pass.send_keys("")
element_botao.click()
# chrome.quit()