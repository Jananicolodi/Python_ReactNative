from selenium import webdriver
import unittest
class TestesAsserts(unittest.TestCase):
    @classmethod
    def setUp(inst):
        inst.driver = webdriver.Chrome()
        inst.driver.maximize_window()
        inst.driver.get("https://www.iffarroupilha.edu.br/")

    def campo_busca_tamanho(self):
        busca = self.driver.find_element_by_xpath("//input[@type='text']")
        busca_tamanho_maximo = int( busca.get_attribute("maxlength"))
        self.assertTrue(busca_tamanho_maximo > 1000 )


    def campo_busca_nome(self):
        busca = self.driver.find_element_by_xpath("//input[@type='text']")
        busca_nome = busca.get_attribute("name")
        self.assertEqual(busca_nome,'searchword')


    def classe_img(self):
        busca = self.driver.find_element_by_xpath("//img[@class='access-button']")
        self.assertNotEqual(busca,'Acesso')


    def verificar_largura(self):
        img = self.driver.find_element_by_xpath("//img[@src='src=\"/modules/mod_gtranslate/tmpl/lang/16/pt-br.png\"']")
        img_altura = int(img.get_attribute("width"))
        self.assertLess(img_altura,'500')

    def tipo_button(self):
        busca_button = self.driver.find_element_by_xpath("button[@type='submit']")
        busca_tipo = busca_button.get_attribute("typ")
        self.assertIsNone(busca_tipo)
    
    def div_classe_span3(self):
        classe_mae = self.driver.find_element_by_xpath("//div[@class='container']")
        busca_classe = self.driver.find_element_by_xpath("//div[@class='span3']")
        self.assertIn(busca_classe,classe_mae)

    def localizar_a_id(self):
        busca = self.driver.find_element_by_xpath("//a[@id='topo']")
        busca_nome = busca.get_attribute("id")
        self.assertNotEqual(busca_nome,'teste')
    
    def h2(self):
        busca_h2 = self.driver.find_element_by_css_selector('h2.hide')
        font_h2 = busca_h2.get_attribute("font")
        self.assertNotAlmostEqual( font_h2,10)
    
    def a_title(self):
        busca_a = self.driver.find_element_by_xpath("//a[@class='pic-gov']")
        classe_a= busca_a.get_attribute("title")
        self.assertEqual(classe_a,"GovBR")


    def classe_span(self):
        busca_classe = self.driver.find_element_by_xpath("//span[@class='portal-title-1']")
        classe_span= busca_classe.get_attribute("class")
        self.assertNotEqual(classe_span,'esperanca')  


if __name__ == '__main__':
    unittest.main()

