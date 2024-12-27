import numpy as np
from tqdm import tqdm
from numba import njit


@njit
def does_it_loop(orig_world, obs_pos0, obs_pos1, start_pos0, start_pos1):
    res = False

    world = orig_world.copy()
    world[obs_pos0, obs_pos1] = "#"

    deltas = [
        (-1, 0),
        (0, 1),
        (1, 0),
        (0, -1),
    ]

    directions = np.zeros((world.shape[0], world.shape[1], 4), dtype=np.uint8)
    cur_delta_idx = 0

    cur_pos0 = start_pos0
    cur_pos1 = start_pos1

    world[cur_pos0, cur_pos1] = "X"
    directions[cur_pos0, cur_pos1, cur_delta_idx] = 1

    new_pos0 = cur_pos0 + deltas[cur_delta_idx][0]
    new_pos1 = cur_pos1 + deltas[cur_delta_idx][1]

    while (
        new_pos0 >= 0
        and new_pos0 < world.shape[0]
        and new_pos1 >= 0
        and new_pos1 < world.shape[1]
    ):
        if world[new_pos0, new_pos1] != "#":
            if (
                world[new_pos0, new_pos1] == "X"
                and directions[new_pos0, new_pos1, cur_delta_idx] == 1
            ):
                res = True
                break

            cur_pos0 = new_pos0
            cur_pos1 = new_pos1
            world[cur_pos0, cur_pos1] = "X"
            directions[cur_pos0, cur_pos1, cur_delta_idx] = 1

        elif world[new_pos0, new_pos1] == "#":
            cur_delta_idx = (cur_delta_idx + 1) % 4

        new_pos0 = cur_pos0 + deltas[cur_delta_idx][0]
        new_pos1 = cur_pos1 + deltas[cur_delta_idx][1]

    return res


# %%

# read input.txt containing a matrix of characters into a 2D numpy array
o_world = np.array(
    [list(line.strip()) for line in open("input.txt", "r", encoding="utf-8")]
)

obstacle_pos = np.where(o_world == ".")

tmp = np.where(o_world == "^")
# %%
# %%
num_loops = 0

for i in tqdm(range(len(obstacle_pos[0]))):
    if does_it_loop(
        o_world, obstacle_pos[0][i], obstacle_pos[1][i], tmp[0][0], tmp[1][0]
    ):
        num_loops += 1

print(num_loops)
