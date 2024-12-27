from collections import deque
from copy import deepcopy


def pm(mm, pad=4):
    for i, m in enumerate(mm):
        print(f"{i:02} " + ",".join([f"{x:>{pad}}" for x in m]))


def get_val(mm, pos: complex):
    return mm[int(pos.real)][int(pos.imag)]


def set_val(mm, pos: complex, val):
    mm[int(pos.real)][int(pos.imag)] = val


def bfs(maze):
    # start position
    start_pos = len(maze) - 2 + 1j
    # start direction
    start_dir = 0 + 1j

    queue = deque()

    start = (start_pos, start_dir, 0)  # cur_dir, cur_pos, total
    set_val(maze, start_pos, 0)
    queue.append(start)

    ql = []

    while queue:
        ql.append(len(queue))
        cur_pos, cur_dir, cur_score = queue.popleft()

        # loop over all possible moves
        for new_dir, new_score in [
            (cur_dir, cur_score + 1),
            (cur_dir * 1j, cur_score + 1001),
            (cur_dir * -1j, cur_score + 1001),
        ]:
            new_pos = cur_pos + new_dir
            new_val = get_val(maze, new_pos)

            if new_val in [".", "E"] or (
                isinstance(new_val, int) and new_val > new_score
            ):
                set_val(maze, new_pos, new_score)
                queue.append((new_pos, new_dir, new_score))

    print(max(ql))


def reverse_bfs(maze):
    queue = deque()
    visited = set()
    res = 1

    start_pos = 1 + (len(maze) - 2) * 1j
    start_val = get_val(maze, start_pos)

    queue.append((start_pos, 1 + 0j, start_val))
    queue.append((start_pos, 0 - 1j, start_val))

    while queue:
        cur_pos, cur_dir, cur_score = queue.popleft()

        # loop over all possible moves
        for new_dir, new_score in [
            (cur_dir, cur_score - 1),
            (cur_dir * 1j, cur_score - 1001),
            (cur_dir * -1j, cur_score - 1001),
        ]:
            new_pos = cur_pos + new_dir
            new_val = get_val(maze, new_pos)

            if (
                isinstance(new_val, int)
                and (
                    new_val in [new_score, new_score - 1000]
                )  # new score could have come from a turn and step
                and new_pos not in visited
            ):
                res += 1
                queue.append((new_pos, new_dir, new_score))
                visited.add(new_pos)

    return res


if __name__ == "__main__":
    test = False

    if test:
        fname = "input_test.txt"
    else:
        fname = "input.txt"

    mymap = [list(line.strip()) for line in open(fname, "r", encoding="utf-8")]
    mymap_copy = deepcopy(mymap)

    bfs(mymap)

    n0 = len(mymap)
    n1 = len(mymap[0])

    print(mymap[1][n1 - 2])

    print(reverse_bfs(mymap))
