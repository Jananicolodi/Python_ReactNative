from selenium import webdriver
import unittest

class TestesAsserts(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.driver = webdriver.Chrome()
        inst.driver.maximize_window()
        inst.driver.get("https://panambi.atende.net/")
    #OK
    def test_alt_img(self):
        img = self.driver.find_element_by_xpath("//img[@class='ban-ai']")
        img_alt = img.get_attribute("alt")
        self.assertEqual(img_alt,'Selo McAffe')
        #input
    def test_class_input(self):
        input_busca = self.driver.find_element_by_xpath("//input[@id='wpo_plugin_menu_superior_campo_busca']")
        input_busca_class = input_busca.get_attribute("class")
        self.assertNotEqual(input_busca_class, 'classes' )

    def test_maxlength_input(self):
        input_busca = self.driver.find_element_by_xpath("//input[@id='wpo_plugin_menu_superior_campo_busca']")
        input_busca_maxlength = input_busca.get_attribute("maxlength")
        self.assertIsNone(input_busca_maxlength)

        #div
    def test_class_div(self):
        div1 = self.driver.find_elements_by_class_name("row")
        busca_classe = self.driver.find_elements_by_class_name("box-menul-mobile")
        self.assertNotIn(busca_classe,div1)
    #a
    def test_title_a(self):
        busca_a = self.driver.find_element_by_xpath("//a[@class='wpo-campo-tem-rs']")
        title_a= busca_a.get_attribute("title")
        self.assertTrue(title_a,"a")


    def test_id_span(self):
        class_span = self.driver.find_element_by_xpath("//span[@class='autoatendimento_ativo selecionado']")
        id_span = class_span.get_attribute("id")
        self.assertEqual(id_span,'aba-servicos')    




    def test_width_div(self):
        width_div = self.driver.find_element_by_xpath("//input[@type='password']")
        width = int(width_div.get_attribute("maxlength"))
        self.assertLess(width, 500)

    def test_img_id(self):
        alt_img = self.driver.find_element_by_xpath("//img[@alt='PREFEITURA MUNICIPAL DE PANAMBI']")
        id_img = alt_img.get_attribute("id")
        self.assertNotEqual(id_img,'submit')




    def test_useenter_input(self):
        id_input = self.driver.find_element_by_xpath("//input[@id='wpo_plugin_menu_superior_campo_busca']")
        useenter_input= id_input.get_attribute("useenter")
        self.assertNotEqual(useenter_input,'true')  


    def test_data_area_section(self):
        id_section = self.driver.find_element_by_xpath("//section[@id='plugin-autoatendimento']")
        data_area = id_section.get_attribute("data-area")
        self.assertTrue( data_area, "autoatendimento" )

    
    


if __name__ == '__main__':
    unittest.main()

