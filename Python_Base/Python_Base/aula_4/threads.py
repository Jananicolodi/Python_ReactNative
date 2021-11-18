from threading import Thread

class MyThread(Thread):

    def __init__(self,num):
        Thread.__init__(self)
        self.num = num

    def run(self):
        print("Mensagem")
        print("Numero: " +str(self.num))

t1 = MyThread(1)
t2 = MyThread(2)

t1.start()
t2.start()
