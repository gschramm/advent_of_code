import numpy as np


with open("input.txt", "r", encoding="UTF-8") as f:
    data = np.array([list(x.strip()) for x in f.readlines()], dtype=int)

# calculate the forward difference along rows
d_row_fwd = np.zeros_like(data)
d_row_fwd[:-1, :] = data[1:, :] - data[:-1, :]

d_row_back = np.zeros_like(data)
d_row_back[1:, :] = -d_row_fwd[:-1, :]

d_col_fwd = np.zeros_like(data)
d_col_fwd[:, :-1] = data[:, 1:] - data[:, :-1]

d_col_back = np.zeros_like(data)
d_col_back[:, 1:] = -d_col_fwd[:, :-1]

directions = np.array([[1, 0], [-1, 0], [0, 1], [0, -1]])

allowed_steps = np.array(
    [d_row_fwd == 1, d_row_back == 1, d_col_fwd == 1, d_col_back == 1]
)

# get all trail head positions
trail_head_coords = np.array(np.where(data == 0)).T

total = 0

for i_th, coord in enumerate(trail_head_coords):
    height = 0
    print("trail head:", i_th, coord[0], coord[1])

    possible_dirs = directions[np.where(allowed_steps[:, coord[0], coord[1]])[0]]
    # update coord
    coord = coord + possible_dirs
    height += 1  # = 1

    while height < 9:
        new_coords = []
        for c in coord:
            possible_dirs = directions[np.where(allowed_steps[:, c[0], c[1]])[0]]
            new_coords.append(c + possible_dirs)

        coord = np.unique(np.vstack(new_coords), axis=0)
        height += 1  # = 2

    total += coord.shape[0]

print(total)
