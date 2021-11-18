from Lista import Lista
from Media import Media
from Diferentes import Diferentes
from Senha import Senha
from Par import Par 
from Maior import Maior
from Email import Email

import re
import unittest

# teste = "a@b.c"
# t = re.findall("@gmail.com",teste)
# e = Email(teste)
class Teste(unittest.TestCase):
    def setUp(self):
        self.n1 = 2
        self.n2 = 3
    def Diferentes(self):
        self.assertNotEqual(self.n1,self.n2)
if __name__ == ' __main__':
    unittest.main()


