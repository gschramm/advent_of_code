import numpy as np


def print_world(arr):
    for row in arr:
        print("".join(row))


if __name__ == "__main__":

    test = False

    if test:
        world_fname = "world_test.txt"
        steps_fname = "steps_test.txt"
    else:
        world_fname = "world.txt"
        steps_fname = "steps.txt"

    orig_world = [
        list(line.strip()) for line in open(world_fname, "r", encoding="utf-8")
    ]

    world = []

    for line in orig_world:
        world.append(
            list(
                "".join(
                    [
                        (
                            "##"
                            if char == "#"
                            else (
                                ".."
                                if char == "."
                                else (
                                    "[]"
                                    if char == "O"
                                    else "@." if char == "@" else char
                                )
                            )
                        )
                        for char in line
                    ]
                )
            )
        )

    world = np.array(world)

    with open(steps_fname, "r", encoding="utf-8") as f:
        steps = list("".join([x.strip() for x in f.readlines()]))

    cur_pos = np.where(world == "@")
    cur_i, cur_j = cur_pos[0][0], cur_pos[1][0]

    for i_step, step in enumerate(steps):
        # print_world(world)
        print(i_step, step)

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
        elif world[new_i, new_j] == "]" and step == "<":
            j = 2
            while (
                world[new_i + j * (new_i - cur_i), new_j + j * (new_j - cur_j)] == "]"
            ):
                j += 2

            if world[new_i + j * (new_i - cur_i), new_j + j * (new_j - cur_j)] == "#":
                continue
            elif world[new_i + j * (new_i - cur_i), new_j + j * (new_j - cur_j)] == ".":
                world[cur_i, cur_j] = "."
                world[new_i, new_j] = "@"
                world[cur_i, (new_j - j) : new_j : 2] = "["
                world[cur_i, (new_j - j + 1) : new_j : 2] = "]"
                cur_i, cur_j = new_i, new_j
        elif world[new_i, new_j] == "[" and step == ">":
            j = 2
            while (
                world[new_i + j * (new_i - cur_i), new_j + j * (new_j - cur_j)] == "["
            ):
                j += 2

            if world[new_i + j * (new_i - cur_i), new_j + j * (new_j - cur_j)] == "#":
                continue
            elif world[new_i + j * (new_i - cur_i), new_j + j * (new_j - cur_j)] == ".":
                world[cur_i, cur_j] = "."
                world[new_i, new_j] = "@"
                world[cur_i, (new_j + 1) : (new_j + 1 + j) : 2] = "["
                world[cur_i, (new_j + 2) : (new_j + 2 + j) : 2] = "]"
                cur_i, cur_j = new_i, new_j
        elif step == "^":
            # first row above @
            if np.all(world[new_i, new_j] == "["):
                box_js = np.array([cur_j])
            else:
                box_js = np.array([cur_j - 1])

            i = 1

            ind_i = []
            ind_j = []

            # 2nd row above @
            while len(box_js) > 0:
                ind_i += [new_i - (i - 1)] * (2 * len(box_js))
                ind_j += list(box_js)
                ind_j += list(box_js + 1)
                row_box_js = np.where(world[new_i - i, :] == "[")[0]

                tmp = []

                for rj in row_box_js:
                    if any(np.abs(rj - box_js) <= 1):
                        tmp.append(rj)

                box_js = np.array(tmp.copy())
                i += 1

            ind_i = np.array(ind_i)
            ind_j = np.array(ind_j)

            tmp = world.copy()
            tmp[ind_i, ind_j] = "."

            if np.all(tmp[ind_i - 1, ind_j] == "."):
                tmp[ind_i - 1, ind_j] = world[ind_i, ind_j]
                tmp[cur_i, cur_j] = "."
                tmp[cur_i - 1, cur_j] = "@"

                # update world
                world = tmp.copy()
                # update position
                cur_i -= 1
        elif step == "v":
            # first row below @
            if np.all(world[new_i, new_j] == "["):
                box_js = np.array([cur_j])
            else:
                box_js = np.array([cur_j - 1])

            i = 1

            ind_i = []
            ind_j = []

            # 2nd row below @
            while len(box_js) > 0:
                ind_i += [new_i + (i - 1)] * (2 * len(box_js))
                ind_j += list(box_js)
                ind_j += list(box_js + 1)
                row_box_js = np.where(world[new_i + i, :] == "[")[0]

                tmp = []

                for rj in row_box_js:
                    if any(np.abs(rj - box_js) <= 1):
                        tmp.append(rj)

                box_js = np.array(tmp.copy())
                i += 1

            ind_i = np.array(ind_i)
            ind_j = np.array(ind_j)

            tmp = world.copy()
            tmp[ind_i, ind_j] = "."

            if np.all(tmp[ind_i + 1, ind_j] == "."):
                tmp[ind_i + 1, ind_j] = world[ind_i, ind_j]
                tmp[cur_i, cur_j] = "."
                tmp[cur_i + 1, cur_j] = "@"

                # update world
                world = tmp.copy()
                # update position
                cur_i += 1

    print_world(world)

    box_locs = np.where(world == "[")
    gps_sum = 0

    for i in range(len(box_locs[0])):
        gps_sum += 100 * box_locs[0][i] + box_locs[1][i]

    print(gps_sum)
