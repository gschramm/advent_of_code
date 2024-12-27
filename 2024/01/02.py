import numpy as np

data = np.loadtxt("input.txt", dtype = int)

n = data.shape[0]

a = data[:,0]
b = data[:,1]

sim_score = 0

for i in range(n):
    inds = np.where(b == a[i])[0]
    if len(inds) > 0:
        sim_score += a[i]*len(inds)
        print(sim_score)

