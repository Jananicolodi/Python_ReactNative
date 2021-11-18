class Idade():
        def __init__(self,anos):
            self.anos = anos  
            for i in range(len(anos)):
                if( anos[i] <= 18):
                    print("Pessoa deve ser maior de 18 anos")

