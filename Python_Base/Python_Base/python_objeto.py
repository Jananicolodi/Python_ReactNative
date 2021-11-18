from Sistema import Sistema
# from Pessoa import Email
# from Pessoa import Sistema
# from Pessoa import Idade
import platform

# p = Pessoa("Miguel",25)
# p.correr()

# print(platform.machine())

s = Sistema(platform.machine())

print(s.Sistema)
