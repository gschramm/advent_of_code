import numpy as np

rules = np.loadtxt("input_a.txt", delimiter="|", dtype=int)

with open("input_b.txt") as f:
    tmp = [line.strip() for line in f.readlines()]

updates = [np.array(x.split(","), dtype=int) for x in tmp]

total = 0

incorrect_updates = []

for ix, x in enumerate(updates):
    res = True
    for i, rule in enumerate(rules):
        i0 = np.where(x == rule[0])[0]
        i1 = np.where(x == rule[1])[0]

        if len(i0) > 0 and len(i1) > 0:
            if i0[0] > i1[0]:
                # print()
                # print(rule)
                # print(i0[0], i1[0])
                res = False
                break

    if res:
        total += x[len(x) // 2]
        # print(ix, x, total)
    else:
        incorrect_updates.append(x)

print()
print(total)

# with open("incorrect_updates.txt", "w") as f:
#    for update in incorrect_updates:
#        f.write(",".join(map(str, update)) + "\n")
