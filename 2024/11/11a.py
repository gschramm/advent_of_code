import numpy as np


def process(inp, num_blinks=25):
    i = 0

    while i < num_blinks:
        outp = []
        for d in inp:
            if d == 0:
                outp.append(1)
            elif len(str(abs(d))) % 2 == 0:
                d_str = str(d)
                n = len(d_str)
                outp.append(int(d_str[: n // 2]))
                outp.append(int(d_str[(n // 2) :]))
            else:
                outp.append(d * 2024)

        i += 1
        print(i, len(outp))
        inp = outp.copy()

    print(len(outp))

    return len(outp)


if __name__ == "__main__":
    data = np.loadtxt("input.txt", dtype=int).tolist()
    res = process(data.copy())
