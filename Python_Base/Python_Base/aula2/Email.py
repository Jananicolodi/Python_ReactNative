class Email():
        def __init__(self,email):
            self.email = email
            if email.find('@'):
                formato = email.split('@')                
                if formato[1] == 'gmail.com':
                    print("Formato válido")
                else:
                    print("Extensão inválida")
            else:
                print("Formato inválido")


