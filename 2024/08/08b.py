import numpy as np
from itertools import combinations

antenna_locations = np.array(
    [list(line.strip()) for line in open("input.txt", "r", encoding="utf-8")]
)

n0, n1 = antenna_locations.shape

antenna_frequencies = np.unique(antenna_locations[antenna_locations != "."])

antinode_map = np.zeros(antenna_locations.shape, dtype=np.uint8)

for i, antenna_frequency in enumerate(antenna_frequencies):
    antenna_locs = np.where(antenna_locations == antenna_frequency)
    antenna_map = np.zeros(antenna_locations.shape, dtype=int)
    antenna_map[antenna_locs] = 1

    antenna_coords = np.array(antenna_locs).T
    # print(antenna_coords)

    for antenna_coords_comb in list(combinations(antenna_coords, 2)):
        antenna_coords0 = antenna_coords_comb[0]
        antenna_coords1 = antenna_coords_comb[1]

        delta = antenna_coords1 - antenna_coords0

        i = 0

        while True:
            new_coords00 = antenna_coords0[0] + i * delta[0]
            new_coords01 = antenna_coords0[1] + i * delta[1]
            if (
                new_coords00 >= 0
                and new_coords00 < n0
                and new_coords01 >= 0
                and new_coords01 < n1
            ):
                antinode_map[new_coords00, new_coords01] = 1

                i += 1
            else:
                break

        j = -1

        while True:
            new_coords00 = antenna_coords0[0] + j * delta[0]
            new_coords01 = antenna_coords0[1] + j * delta[1]
            if (
                new_coords00 >= 0
                and new_coords00 < n0
                and new_coords01 >= 0
                and new_coords01 < n1
            ):
                antinode_map[new_coords00, new_coords01] = 1

                j -= 1
            else:
                break


print(antinode_map.sum())
