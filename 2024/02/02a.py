import numpy as np


def readfile(filename):
    with open(filename, "r") as file:
        lines = file.read().splitlines()

    return [np.array(x.split(" "), dtype=int) for x in lines]


data = readfile("input.txt")

num_safe = 0

for i, x in enumerate(data):
    diff = np.diff(x)
    abs_diff = np.abs(diff)

    if (abs_diff.max() <= 3) and (abs_diff.min() >= 1):
        if np.unique(np.sign(diff)).shape[0] == 1:
            num_safe += 1
            print(i, x)
            print(diff)
            print()
        else:
            q = 1

print(num_safe)
