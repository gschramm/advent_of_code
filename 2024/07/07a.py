def reduce_list(x):
    xx = x.copy()

    a = xx.pop(0)
    xx2 = xx.copy()

    xx[0] += a
    xx2[0] *= a

    return [xx, xx2]


def possible_results(x):
    res = reduce_list(x)

    i = 1
    while len(res[0]) > 1:
        tmp = [reduce_list(z) for z in res]
        res = []
        for j in range(2**i):
            res.append(tmp[j][0])
            res.append(tmp[j][1])
        i += 1

    res = [item for sublist in res for item in sublist]

    return res


# %%

with open("input.txt") as f:
    lines = [line.strip() for line in f.readlines()]

test_results = []
numbers = []

for x in lines:
    tmpstr = x.split(":")
    test_results.append(int(tmpstr[0]))
    numbers.append([int(t) for t in tmpstr[1].strip().split(" ")])

total = 0

for i, test_result in enumerate(test_results):
    if test_result in possible_results(numbers[i]):
        total += test_result

print(total)
