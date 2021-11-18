from selenium import webdriver

chrome = webdriver.Chrome()
chrome.maximize_window()
# chrome.back()
chrome.get("http://google.com")

element_viewport = chrome.find_element_by_id("viewport")

chrome.execute_script("arguments[0].style = 'background-color:blue'",element_viewport)

element_logo = chrome.find_element_by_id("hplogo")
chrome.execute_script("arguments[0].width=600",element_logo)

element_btn = chrome.find_elements_by_name("btnI")[1]
chrome.execute_script("arguments[0].value='Estou sem sorte'",element_btn)

elements_input = chrome.find_elements_by_tag_name("input")
for elem in elements_input:
    chrome.execute_script("arguments[0].style ='color:red'",elem)

elements_input = chrome.find_elements_by_tag_name("a")
for elem in elements_input:
    chrome.execute_script("arguments[0].style ='color:green'",elem)


element_pesquisa = chrome.find_element_by_name("q")
element_pesquisa.send_keys("iFFar")

element_submit = chrome.find_elements_by_name("btnK")[1]
element_submit.click()