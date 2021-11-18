from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

chrome = webdriver.Chrome(ChromeDriverManager().install())# Desktop\TSI\Python_Base\Python_Base\aula_8>python selenium.py

# chrome = webdriver.Chrome()
chrome.maximize_window()
chrome.get("http://google.com")

search = chrome.find_element_by_name("q")
search.send_keys("ppc iffar panambi")

search_btn = chrome.find_elements_by_name("btnK")[1]
search_btn.click()

content = chrome.find_element_by_id("rso")
links = content.find_elements_by_tag_name("a")
links[0].click()

ppc_file = chrome.find_element_by_link_text("Tecnologia em Sistemas para Internet")
ppc_file.click()