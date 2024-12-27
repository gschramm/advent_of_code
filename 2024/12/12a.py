import numpy as np
from scipy.ndimage import binary_dilation, label, binary_fill_holes


def calculate_perimeter(img):
    """
    Calculate the perimeter of a region in a binary image (0s and 1s).

    Parameters:
        img (np.ndarray): 2D binary image with 0s and 1s.

    Returns:
        int: The perimeter of the region.
    """
    # Find the coordinates of pixels with value 1
    coordinates = np.array(np.where(img == 1)).T  # Transpose to get (row, col) pairs

    # Initialize perimeter
    perimeter = 0

    # Iterate through the coordinates of region pixels
    for i, j in coordinates:
        # Check its 4-connected neighbors
        if i == 0 or img[i - 1, j] == 0:  # Top neighbor
            perimeter += 1
        if i == img.shape[0] - 1 or img[i + 1, j] == 0:  # Bottom neighbor
            perimeter += 1
        if j == 0 or img[i, j - 1] == 0:  # Left neighbor
            perimeter += 1
        if j == img.shape[1] - 1 or img[i, j + 1] == 0:  # Right neighbor
            perimeter += 1

    return perimeter


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
