import numpy as np


def readfile(filename):
    with open(filename, "r") as file:
        lines = file.read().splitlines()

    return [np.array(x.split(" "), dtype=int) for x in lines]


def is_safe(report):
    diff = np.diff(report)
    abs_diff = np.abs(diff)

    res = False

    if (abs_diff.max() <= 3) and (abs_diff.min() >= 1):
        if np.unique(np.sign(diff)).shape[0] == 1:
            res = True

    return res


if __name__ == "__main__":
    data = readfile("input.txt")

    num_safe = 0

    for i, x in enumerate(data):
        if is_safe(x):
            num_safe += 1
        else:
            # check if we can make the report safe by removing one element
            for j in range(len(x)):
                x_new = np.delete(x, j)
                if is_safe(x_new):
                    num_safe += 1
                    break

    print(num_safe)
