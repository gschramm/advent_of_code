import numpy as np

# read input.txt containing a matrix of characters into a 2D numpy array
world = np.array(
    [list(line.strip()) for line in open("input.txt", "r", encoding="utf-8")]
)

cur_pos = np.where(world == "^")
world[cur_pos] = "X"
cur_delta = (np.array([-1]), np.array([0]))

# %%

new_pos = (cur_pos[0] + cur_delta[0], cur_pos[1] + cur_delta[1])

i = 0

while (
    new_pos[0] >= 0
    and new_pos[0] < world.shape[0]
    and new_pos[1] >= 0
    and new_pos[1] < world.shape[1]
):
    if world[new_pos] != "#":
        cur_pos = new_pos
        world[cur_pos] = "X"
        new_pos = (cur_pos[0] + cur_delta[0], cur_pos[1] + cur_delta[1])

    elif world[new_pos] == "#":
        if cur_delta == (np.array([-1]), np.array([0])):
            cur_delta = (np.array([0]), np.array([1]))
        elif cur_delta == (np.array([0]), np.array([1])):
            cur_delta = (np.array([1]), np.array([0]))
        elif cur_delta == (np.array([1]), np.array([0])):
            cur_delta = (np.array([0]), np.array([-1]))
        elif cur_delta == (np.array([0]), np.array([-1])):
            cur_delta = (np.array([-1]), np.array([0]))

        new_pos = (cur_pos[0] + cur_delta[0], cur_pos[1] + cur_delta[1])

    i += 1

# save world to output.txt
with open("output.txt", "w", encoding="utf-8") as f:
    for row in world:
        f.write("".join(row) + "\n")
