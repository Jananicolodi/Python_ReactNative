import numpy as np
from timeit import default_timer as timer
from numba import jit
x = np.arange(9000000).reshape(3000,3000)

@jit(nopython=True)
def opr_matrix(a):
    for i in range(a.shape[0]):
        for j in range(a.shape[1]):
            a[i,j] = np.tanh(a[i,j])
    return a
t = timer()
opr_matrix(x)
print(timer()-t)
t = timer()
opr_matrix(x)
print(timer()-t)