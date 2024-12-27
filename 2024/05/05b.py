import numpy as np

rules = np.loadtxt("input_a.txt", delimiter="|", dtype=int)

with open("incorrect_updates.txt") as f:
    tmp = [line.strip() for line in f.readlines()]

incorrect_updates = [np.array(x.split(","), dtype=int) for x in tmp]

total = 0

for ix, x in enumerate(incorrect_updates):
    x_new = np.array([], dtype=int)

    for i_num, num in enumerate(x):
        if i_num == 0:
            x_new = np.append(x_new, num)
        else:
            n = len(x_new)
            # get the rules that are affected by the number
            nums_before = rules[np.where(rules[:, 0] == num), 1]
            nums_after = rules[np.where(rules[:, 1] == num), 0]

            # get all indices of x_new that contain any of the numbers in nums_before
            inds_before = np.where(np.isin(x_new, nums_before))[0]
            if len(inds_before) > 0:
                i_before = inds_before.min()
            else:
                i_before = n

            # get all indices of x_new that contain any of the numbers in nums_after
            inds_after = np.where(np.isin(x_new, nums_after))[0]

            if len(inds_after) > 0:
                i_after = inds_after.max()
            else:
                i_after = -1

            if i_before < i_after:
                breakpoint()

            # insert num into x_new at position i_after
            x_new = np.insert(x_new, i_after + 1, num)

    print(ix, x, x_new)

    total += x_new[len(x_new) // 2]

    # check if x_new is correct
    res = True
    for i, rule in enumerate(rules):
        i0 = np.where(x_new == rule[0])[0]
        i1 = np.where(x_new == rule[1])[0]

        if len(i0) > 0 and len(i1) > 0:
            if i0[0] > i1[0]:
                print()
                print(rule)
                print(i0[0], i1[0])
                res = False
                breakpoint()
                break


print()
print(total)
