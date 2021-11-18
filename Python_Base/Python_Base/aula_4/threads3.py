from math import sqrt
from timeit import default_timer as timer
from multiprocessing import Pool
import sys

l = [1]* 10000000
res = [0]* len(l)

thread = int(sys.argv[1])

part_size = int(len(l)/thread)

def SumVectors(j):
    num = l[j*part_size:(j+1)*part_size]
    j *= part_size
    for i in range(len(num)):
        res[j] = num[i] + num[i] - num[i] * 2 + sqrt(num[i])
        j+=1

if __name__ == '__main__':
    index = []
    for i in range(thread):
        index.append(i)
    t1 = timer()
    with Pool(thread) as p:
        p.map(SumVectors,index)
    print(timer()-t1)
