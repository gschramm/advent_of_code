import numpy as np

test = False

if test:
    fname = "input_test.txt"
    thresh = 20
else:
    fname = "input.txt"
    thresh = 100

tmp = np.array([list(line.strip()) for line in open(fname, "r", encoding="utf-8")])

maze = np.zeros(tmp.shape, dtype=np.uint8)
maze[tmp == "#"] = 1
maze[tmp == "S"] = 2
maze[tmp == "E"] = 3

# %%
pos = np.where(maze == 2)
pos = (pos[0][0], pos[1][0])

val = maze[pos]
direction = 0 - 1j
counter = 0

nodes = [pos]
verbose = False

# %%
while val != 3 and counter < 1000000:

    if verbose:
        print(counter, pos, direction)

    new_pos = pos[0] + int(direction.real), pos[1] + int(direction.imag)

    if maze[new_pos] != 1:
        pos = new_pos
        val = maze[pos]
    else:
        # turn right
        direction *= -1j
        new_pos = pos[0] + int(direction.real), pos[1] + int(direction.imag)
        if maze[new_pos] != 1:
            pos = new_pos
            val = maze[pos]
        else:
            # turn left
            direction *= -1
            new_pos = pos[0] + int(direction.real), pos[1] + int(direction.imag)
            if maze[new_pos] != 1:
                pos = new_pos
                val = maze[pos]
            else:
                raise ValueError("No path found")
    nodes.append(pos)
    counter += 1

# %%
print(len(nodes))
# %%
num_cheats = 0

for i, node in enumerate(nodes[:-thresh]):
    future_nodes = np.array(nodes[(i + 1) :])

    # distance_to_future_nodes = np.linalg.norm(future_nodes - np.array(node), axis=1)
    distance_to_future_nodes = np.linalg.norm(
        future_nodes - np.array(node), axis=1, ord=1
    )

    cheat_nodes_pos = []
    cheat_times = []

    for cheat_time in [2]:
        tmp = np.where(distance_to_future_nodes == cheat_time)[0].tolist()
        cheat_nodes_pos += tmp
        cheat_times += [cheat_time] * len(tmp)

    cheat_nodes_pos = np.array(cheat_nodes_pos)
    cheat_times = np.array(cheat_times)

    if len(cheat_nodes_pos) > 0:
        steps_saved = cheat_nodes_pos - cheat_times + 1
        num_cheats += len(np.where(steps_saved >= thresh)[0])
        # print(i, node, cheat_nodes_pos, steps_saved)

print(thresh, num_cheats)
