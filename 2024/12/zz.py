import numpy as np
from skimage.measure import find_contours

# Example usage
img = np.array(
    [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 1, 0],
        [0, 1, 1, 1, 0, 0, 1, 0],
        [0, 1, 1, 1, 0, 0, 1, 0],
        [0, 1, 0, 0, 1, 1, 1, 0],
        [0, 1, 0, 0, 1, 1, 1, 0],
        [0, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
    ]
)

# count the number of straight sides

c = find_contours(img)[0]
d = c[1:,] - c[:-1]

num_straight_sides = np.where(np.linalg.norm(d, axis=1) != 1)[0].size

print(num_straight_sides)
