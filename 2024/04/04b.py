import numpy as np


def match_2d_pattern(arr, pattern_2d):
    res = True

    if arr[0, 0] != pattern_2d[0, 0]:
        res = False
    if arr[0, 2] != pattern_2d[0, 2]:
        res = False
    if arr[1, 1] != pattern_2d[1, 1]:
        res = False
    if arr[2, 0] != pattern_2d[2, 0]:
        res = False
    if arr[2, 2] != pattern_2d[2, 2]:
        res = False

    return res


with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines()]

array = np.array([list(line) for line in lines])

# loop over all 3x3 subarrays
pat2d = np.array([["M", ".", "S"], [".", "A", "."], ["M", ".", "S"]])


total = 0

for i in range(array.shape[0] - 2):
    for j in range(array.shape[1] - 2):
        subarray = array[i : i + 3, j : j + 3]

        if match_2d_pattern(subarray, pat2d):
            total += 1

        if match_2d_pattern(subarray, pat2d.T):
            total += 1

        if match_2d_pattern(subarray, np.fliplr(pat2d)):
            total += 1

        if match_2d_pattern(subarray, np.fliplr(pat2d).T):
            total += 1


print(total)
