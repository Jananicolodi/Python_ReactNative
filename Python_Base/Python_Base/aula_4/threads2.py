from threading import Thread
from math import sqrt
from timeit import default_timer as timer

class MyThread(Thread):

    def __init__(self,num):
        Thread.__init__(self)
        self.res = [0]*len(num)
        self.num = num

    def run(self):
      for i in range(len(self.num)):
          self.res[i] = self.num[i] + self.num[i] - self.num[i]*2 + sqrt(self.num[i])

l = [1]* 10000000

l1 = l[0:int(len(l)/2)]
l2 = l[int(len(l)/2):]

t1 = MyThread(l1)
t2 = MyThread(l2)
tempo_1 = timer()
t1.start()
t2.start()
t1.join()
t2.join()
print(timer() - tempo_1)
