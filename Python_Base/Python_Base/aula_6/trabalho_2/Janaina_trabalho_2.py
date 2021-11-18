from selenium import webdriver
import unittest

class TestesAsserts(unittest.TestCase):

    @classmethod
    def setUpClass(inst):
        inst.driver = webdriver.Chrome()
        inst.driver.maximize_window()
        inst.driver.get("https://www.iffarroupilha.edu.br/")


    def test_a_title(self):
        busca_a = self.driver.find_element_by_xpath("//a[@class='pic-gov']")
        classe_a= busca_a.get_attribute("title")
        self.assertEqual(classe_a,"GovBR")


    def test_campo_busca_nome(self):
        busca = self.driver.find_element_by_xpath("//input[@type='text']")
        busca_nome = busca.get_attribute("name")
        self.assertEqual(busca_nome,'searchword')


    def test_classe_img(self):
        busca = self.driver.find_element_by_xpath("//img[@class='access-button']")
        self.assertNotEqual(busca,'Acesso')


    def test_localizar_a_id(self):
        busca = self.driver.find_element_by_xpath("//a[@id='topo']")
        busca_nome = busca.get_attribute("id")
        self.assertNotEqual(busca_nome,'teste')    


    def test_classe_span(self):
        busca_classe = self.driver.find_element_by_xpath("//span[@class='portal-title-1']")
        classe_span= busca_classe.get_attribute("class")
        self.assertNotEqual(classe_span,'esperanca')  


    def test_campo_busca_tamanho(self):
        busca = self.driver.find_element_by_xpath("//input[@type='text']")
        busca_tamanho_maximo = busca.get_attribute("maxlength")
        self.assertIsNone(busca_tamanho_maximo)


    def test_img(self):
        busca = self.driver.find_element_by_xpath("//img[@alt='es']")
        width_img = int(busca.get_attribute("width"))
        self.assertTrue( width_img < 1000 )
    

    def test_verificar_largura(self):
        img = self.driver.find_element_by_xpath("//img[@alt='entrada_portal.png']")
        img_altura = int(img.get_attribute("width"))
        self.assertLess(img_altura, 500)
    
    
    def test_div_classe_span3(self):
        classe_mae = self.driver.find_elements_by_class_name("container")
        busca_classe = self.driver.find_elements_by_class_name("span3")
        self.assertNotIn(busca_classe,classe_mae)
    

    def test_classe_button(self):
        busca = self.driver.find_element_by_xpath("//button[@class='btn searchButton']")
        busca_nome = busca.get_attribute("type")
        self.assertEqual(busca_nome,'submit')

    def test_classe_div(self):
        busca = self.driver.find_element_by_xpath("//div[@id='portal-searchbox']")
        busca_nome = busca.get_attribute("class")
        self.assertEqual(busca_nome,'row')

if __name__ == '__main__':
    unittest.main()

