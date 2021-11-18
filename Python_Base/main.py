import unittest
import numpy
import sys

class TesteSkips(unittest.TestCase):

	@unittest.skip("Skip demonstrativo")
	def teste_falha(self):
		self.fail("Falha explicita")
	
	@unittest.skipIf(numpy.__version__ < '1.19',"versão da biblioteca não compativel")
	def teste_numpy(self):
		print("testando biblioteca numpy...")
	
	@unittest.skipUnless(sys.platform.startswith("lin"),"requer windows")
	def testa_so(self):
		print("testando sistema operacional")

if __name__ == '__main__':
	unittest.main()