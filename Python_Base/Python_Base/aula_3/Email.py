class Email():
            def __init__(self,email):
                self.email = email
                # self.assertRegex(email)
                if len(email) == 0 :
                    print("Informe um e-mail válido")
                else:
                    print(email)
