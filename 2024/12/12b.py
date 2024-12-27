import numpy as np
from scipy.ndimage import binary_dilation, label, binary_fill_holes
from skimage.measure import find_contours


def calculate_perimeter(img):
    c = find_contours(img)[0]
    d = c[1:,] - c[:-1]
    return np.where(np.linalg.norm(d, axis=1) != 1)[0].size


with open("input.txt", "r", encoding="UTF-8") as f:
    data = np.array([list(x.strip()) for x in f.readlines()])

    # convert chars to integers A = 1 ... Z = 26
    # data = np.array([[ord(char) - ord("A") + 1 for char in row] for row in data])

nums = np.unique(data)

# pad with 0s
data = np.pad(data, 1)

price = 0

for i, num in enumerate(nums):
    num_mask = (data == num).astype(int)
    labels, num_labels = label(num_mask)

    num_price = 0

    for lab in np.arange(1, num_labels + 1):
        area = 0
        perim = 0

        binary_mask = (labels == lab).astype(int)
        area += binary_mask.sum()

        # Fill holes to calculate the external perimeter
        filled_mask = binary_fill_holes(binary_mask).astype(int)
        dilated_filled = binary_dilation(filled_mask).astype(int)
        external_boundary = dilated_filled - filled_mask

        # add external perimeter
        perim += calculate_perimeter(filled_mask)

        # Internal holes boundary (subtract the original binary mask from the filled mask)
        holes_mask = filled_mask - binary_mask
        hole_labels, num_holes = label(holes_mask)

        for hole_lab in np.arange(1, num_holes + 1):
            hole_mask = (hole_labels == hole_lab).astype(int)
            dilated_hole = binary_dilation(hole_mask).astype(int)
            internal_holes_boundary = dilated_hole - hole_mask

            # add perimeter of each hole
            perim += calculate_perimeter(hole_mask)

        num_price += area * perim
        # print(num, area, perim)

    # print(num, num_price)
    price += num_price

print(price)
