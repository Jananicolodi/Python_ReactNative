from selenium import webdriver
import unittest

class TestesAsserts(unittest.TestCase):
    @classmethod
    def setUp(inst):
        inst.driver = webdriver.Chrome()
        inst.driver.maximize_window()
        inst.driver.get("https://www.google.com.br")


    def test_search_field_name(self):
        search_field = self.driver.find_element_by_xpath("//input[@type='text']")
        search_field_name = search_field.get_attribute("name")
        self.assertEqual(search_field_name,'q')

    def test_country(self):
        country = self.driver.find_element_by_xpath("//span[@class='Q8LRLc']")
        self.assertNotEqual(country.text,'Inglaterra')

    def test_search_field_length(self):
        search_field = self.driver.find_element_by_xpath("//input[@type='text']")
        search_field_max_length = int( search_field.get_attribute("maxlength"))
        self.assertTrue(search_field_max_length > 1000 )


    def test_attribute(self):
        btn = self.driver.find_element_by_class_name('gNO89b')
        type_btn = btn.get_attribute("typ")
        self.assertIsNone(type_btn)

    def test_btn_inside_listbtn(self):
        inputs = self.driver.find_element_by_class_name("input")
        btn_search = self.driver.find_element_by_name("btnk") [1]
        self.assertIn(btn_search,inputs)

if __name__ == '__main__':
    unittest.main()

