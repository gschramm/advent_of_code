# not solved without reading the subreddit
# main learning: recursion with caching can be very powerful
#                functool implements caching with the cache decorator

import numpy as np
import functools
from time import time


@functools.cache
def single_blink_single_stone(d):
    if d == 0:
        res = (1, None)
    elif len(str(abs(d))) % 2 == 0:
        d_str = str(d)
        n = len(d_str)
        res = (int(d_str[: n // 2]), int(d_str[(n // 2) :]))
    else:
        res = (d * 2024, None)

    return res


@functools.cache
def count_single_stone(val, depth):

    left_stone, right_stone = single_blink_single_stone(val)

    if depth == 1:
        if right_stone is None:
            return 1
        else:
            return 2
    else:
        # recurse to the next level
        # if the right stone is None, we only have one stone and simply recurse
        output = count_single_stone(left_stone, depth - 1)

        # if the right stone is not None, we have two stones and we need to also
        # add the results of the right stone
        if right_stone is not None:
            output += count_single_stone(right_stone, depth - 1)

        return output


def process_data(data, depth):
    total = 0

    for d in data:
        total += count_single_stone(d, depth)

    return total


if __name__ == "__main__":
    data = np.loadtxt("input.txt", dtype=int).tolist()

    t0 = time()
    print(process_data(data, 75))
    t1 = time()
    print(t1 - t0)
