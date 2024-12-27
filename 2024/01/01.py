import numpy as np

data = np.loadtxt("input.txt", dtype = int)

a = data[:,0]
b = data[:,1]

a = np.sort(a)
b = np.sort(b)

res = np.abs(a-b).sum()

print(res)
