from collections import deque
from copy import deepcopy


def pm(mm, pad=4):
    for i, m in enumerate(mm):
        print(f"{i:02} " + ",".join([f"{x:>{pad}}" for x in m]))


def get_val(mm, pos: complex):
    return mm[int(pos.real)][int(pos.imag)]


def set_val(mm, pos: complex, val):
    mm[int(pos.real)][int(pos.imag)] = val


if __name__ == "__main__":
    test = True

    if test:
        fname = "input_test.txt"
    else:
        fname = "input.txt"

    maze = [list(line.strip()) for line in open(fname, "r", encoding="utf-8")]

    maze_copy = deepcopy(maze)

    n0 = len(maze)
    n1 = len(maze[0])

    # start position
    start_pos = n0 - 2 + 1j
    # start direction
    start_dir = 0 + 1j

    queue = deque()

    start = (start_pos, start_dir, 0)  # cur_dir, cur_pos, total
    set_val(maze, start_pos, 0)
    queue.append(start)

    while queue:
        cur_pos, cur_dir, cur_score = queue.popleft()

        # loop over all possible moves
        for new_dir, new_score in [
            (cur_dir, cur_score + 1),
            (cur_dir * 1j, cur_score + 1001),
            (cur_dir * -1j, cur_score + 1001),
        ]:
            new_pos = cur_pos + new_dir

            if get_val(maze, new_pos) == "#":
                # invalid move
                continue

            new_val = get_val(maze, new_pos)

            if new_val in [".", "E"] or (
                isinstance(new_val, int) and new_val > new_score
            ):
                set_val(maze, new_pos, new_score)
                queue.append((new_pos, new_dir, new_score))

    print(maze[1][n1 - 2])
