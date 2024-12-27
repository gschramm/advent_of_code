# not solved without reading the subreddit
# main learning: recursion with caching can be very powerful
#                functool implements caching with the cache decorator

import numpy as np
from time import time

# global cache variables
single_blink_cache = {}
count_single_stone_cache = {}

# global variable to store the histogram of single_blink_single_stone
single_blink_histo = {}


def single_blink_single_stone(d):
    if d in single_blink_histo:
        single_blink_histo[d] += 1
    else:
        single_blink_histo[d] = 1

    if d in single_blink_cache:
        return single_blink_cache[d]
    else:
        if d == 0:
            res = (1, None)
        elif len(str(abs(d))) % 2 == 0:
            d_str = str(d)
            n = len(d_str)
            res = (int(d_str[: n // 2]), int(d_str[(n // 2) :]))
        else:
            res = (d * 2024, None)

        single_blink_cache[d] = res

    return res


def count_single_stone(val, depth):

    if (val, depth) in count_single_stone_cache:
        return count_single_stone_cache[(val, depth)]

    left_stone, right_stone = single_blink_single_stone(val)

    if depth == 1:
        if right_stone is None:
            count_single_stone_cache[(val, depth)] = 1
            return 1
        else:
            count_single_stone_cache[(val, depth)] = 2
            return 2
    else:
        # recurse to the next level
        # if the right stone is None, we only have one stone and simply recurse
        output = count_single_stone(left_stone, depth - 1)

        # if the right stone is not None, we have two stones and we need to also
        # add the results of the right stone
        if right_stone is not None:
            output += count_single_stone(right_stone, depth - 1)

        count_single_stone_cache[(val, depth)] = output

        return output


def process_data(data, depth):
    total = 0

    for d in data:
        total += count_single_stone(d, depth)

    return total


if __name__ == "__main__":
    data = np.loadtxt("input.txt", dtype=int).tolist()

    num_iter = 75

    t0 = time()
    res = process_data(data, num_iter)
    t1 = time()

    if num_iter == 25:
        assert res == 197157
    elif num_iter == 75:
        assert res == 234430066982597

    # print single_blink_histo but make sure that keys are sorted
    for k in sorted(single_blink_histo.keys()):
        print(k, single_blink_histo[k])

    print()
    print("result", res)
    print("time", t1 - t0)
