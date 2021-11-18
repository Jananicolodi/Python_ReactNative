from selenium import webdriver
import unittest
class SearchTest(unittest.TestCase):
    @classmethod
    def setUpClass(inst):
        inst.driver = webdriver.Chrome()
        inst.driver.maximize_window()
        inst.driver.get("https://www.google.com.br")

    def test_search_results(self):
        search_field = self.driver.find_element_by_name("q")
        search_field.send_keys("faceboook")
        search_btn = self.driver.find_element_by_name("btnK")[1]
        search_btn.click()

        results = self.driver.find_element_by_class_name("g")
        num_results = len(results)
        self.assertEqual(num_results,8)

    def test_numofimages(self):
        images = self.driver.find_element_by_tag_name("img")
        num_images = len(images)
        self.assertEqual(num_images,2)

if __name__ == '__main__':
    unittest.main()

