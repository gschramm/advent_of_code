import numpy as np

test = False

if test:
    world_fname = "world_test.txt"
    steps_fname = "steps_test.txt"
else:
    world_fname = "world.txt"
    steps_fname = "steps.txt"


world = np.array(
    [list(line.strip()) for line in open(world_fname, "r", encoding="utf-8")]
)

with open(steps_fname, "r", encoding="utf-8") as f:
    steps = list("".join([x.strip() for x in f.readlines()]))

cur_pos = np.where(world == "@")
cur_i, cur_j = cur_pos[0][0], cur_pos[1][0]

# print(world)

for i_step, step in enumerate(steps):
    new_i, new_j = cur_i, cur_j
    if step == "^":
        new_i -= 1
    elif step == "v":
        new_i += 1
    elif step == "<":
        new_j -= 1
    elif step == ">":
        new_j += 1

    if world[new_i, new_j] == "#":
        continue
    elif world[new_i, new_j] == ".":
        world[cur_i, cur_j] = "."
        world[new_i, new_j] = "@"
        cur_i, cur_j = new_i, new_j
    elif world[new_i, new_j] == "O":
        j = 1
        while world[new_i + j * (new_i - cur_i), new_j + j * (new_j - cur_j)] == "O":
            j += 1

        if world[new_i + j * (new_i - cur_i), new_j + j * (new_j - cur_j)] == "#":
            continue
        elif world[new_i + j * (new_i - cur_i), new_j + j * (new_j - cur_j)] == ".":
            world[cur_i, cur_j] = "."
            world[new_i, new_j] = "@"
            world[new_i + j * (new_i - cur_i), new_j + j * (new_j - cur_j)] = "O"
            cur_i, cur_j = new_i, new_j
    else:
        raise ValueError("Invalid world state")

    # print(step)
    # print(world)

box_locs = np.where(world == "O")
gps_sum = 0

for i in range(len(box_locs[0])):
    gps_sum += 100 * box_locs[0][i] + box_locs[1][i]

print(gps_sum)
