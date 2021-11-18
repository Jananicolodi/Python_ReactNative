from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

chrome = webdriver.Chrome(ChromeDriverManager().install())# Desktop\TSI\Python_Base\Python_Base\aula_8>python selenium.py

# chrome = webdriver.Chrome()
chrome.maximize_window()
chrome.get("https://www.youtube.com")

search = chrome.find_element_by_name("search_query")
search.send_keys("laravel")

search_btn = chrome.find_element_by_id("search-icon-legacy")
search_btn.click()

content = chrome.find_element_by_id("dismissable")
links = content.find_element_by_tag_id("dismissable")
links[0].click()

# ppc_file = chrome.find_element_by_link_text("Tecnologia em Sistemas para Internet")
# ppc_file.click()