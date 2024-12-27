import numpy as np


def read_input_file(file_path):
    with open(file_path, "r") as file:
        content = file.read().strip()

    # Split the content into blocks
    blocks = content.split("\n\n")

    # Convert each block into a 2D numpy array
    arrays = [
        np.array([list(map(int, line)) for line in block.split("\n")])
        for block in blocks
    ]

    l = np.array([array for array in arrays if np.all(array[0] == 1)])
    k = np.array([array for array in arrays if np.all(array[-1] == 1)])

    return l, k


if __name__ == "__main__":
    locks, keys = read_input_file("input.txt")

    lock_heights = locks.sum(axis=1) - 1
    key_heights = keys.sum(axis=1) - 1

    total = 0

    for l_height in lock_heights:
        for k_height in key_heights:
            s = l_height + k_height
            if s.max() < 6:
                total += 1

    print(total)
