import numpy as np
import re

with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines()]

array = np.array([list(line) for line in lines])

pattern1 = re.compile(r"XMAS")
pattern2 = re.compile(r"SAMX")

total = 0

# loop over rows
for i in range(array.shape[0]):
    row_str = "".join(array[i, :])
    matches1 = [(m.start(), m.end()) for m in re.finditer(pattern1, row_str)]
    matches2 = [(m.start(), m.end()) for m in re.finditer(pattern2, row_str)]
    total += len(matches1) + len(matches2)

# loop over columns
for j in range(array.shape[1]):
    col_str = "".join(array[:, j])
    matches1 = [(m.start(), m.end()) for m in re.finditer(pattern1, col_str)]
    matches2 = [(m.start(), m.end()) for m in re.finditer(pattern2, col_str)]
    total += len(matches1) + len(matches2)

# loop over all diagonals
for i in range(-(array.shape[0] - 1), array.shape[0]):
    diag_str = "".join(np.diagonal(array, i))
    matches1 = [(m.start(), m.end()) for m in re.finditer(pattern1, diag_str)]
    matches2 = [(m.start(), m.end()) for m in re.finditer(pattern2, diag_str)]
    total += len(matches1) + len(matches2)

# loop over all anti-diagonals
flipped_array = np.fliplr(array)
for i in range(-(array.shape[0] - 1), array.shape[0]):
    diag_str = "".join(np.diagonal(flipped_array, i))
    matches1 = [(m.start(), m.end()) for m in re.finditer(pattern1, diag_str)]
    matches2 = [(m.start(), m.end()) for m in re.finditer(pattern2, diag_str)]
    total += len(matches1) + len(matches2)

print(total)
