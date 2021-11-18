# 2. Depois de escolhido o site, realize 10 testes ou mais dentro desse site
# utilizando a linguagem Python juntamente com o Selenium e o Unittest. Os
# seguintes elementos web devem ser testados ao longo dos 10 testes,
# devendo-se utilizar xpath ao menos em 4 desses para busca dos elementos.
# ● Imagens: <img />
# ● Divs: <div> </div>
# ● a: <a />
# ● inputs: <input />
# 3. Além disso, também devem ser utilizadas ao longo dos 10 testes, as
# seguintes funções do unittest:
# ● assertEqual ou assertNotEqual
# ● assertTrue ou assertFalse
# ● assertIsNone ou assertIsNotNone
# ● assertIn ou assertNotIn
# Os requisitos acima cumprem 80% da nota do trabalho, os outros 20% serão dados
# aos trabalhos que incluíram mais elementos web nas buscas do que os
# apresentados no item 2 deste trabalho, e que também incluírem mais tipos de testes
# do que os presentes no item 3 deste trabalho.
# Bom trabalho, e qualquer dúvida estou a disposição
from selenium import webdriver
import unittest
class TestesAsserts(unittest.TestCase):
    @classmethod
    def setUp(inst):
        inst.driver = webdriver.Edge()
        inst.driver.maximize_window()
        inst.driver.get("https://www.iffarroupilha.edu.br/")


    def test_search_field_name(self):
        search_field = self.driver.find_element_by_xpath("//input[@type='text']")
        search_field_name = search_field.get_attribute("name")
        self.assertEqual(search_field_name,'q')

    # def test_country(self):
    #     country = self.driver.find_element_by_xpath("//span[@class='Q8LRLc']")
    #     self.assertNotEqual(country.text,'Inglaterra')

    # def test_search_field_length(self):
    #     search_field = self.driver.find_element_by_xpath("//input[@type='text']")
    #     search_field_max_length = int( search_field.get_attribute("maxlength"))
    #     self.assertTrue(search_field_max_length > 1000 )


    # def test_attribute(self):
    #     btn = self.driver.find_element_by_class_name('gNO89b')
    #     type_btn = btn.get_attribute("typ")
    #     self.assertIsNone(type_btn)

    # def test_btn_inside_listbtn(self):
    #     inputs = self.driver.find_element_by_class_name("input")
    #     btn_search = self.driver.find_element_by_name("btnk") [1]
    #     self.assertIn(btn_search,inputs)

if __name__ == '__main__':
    unittest.main()

