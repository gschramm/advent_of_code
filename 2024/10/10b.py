import numpy as np
import matplotlib.pyplot as plt
import networkx as nx


with open("input.txt", "r", encoding="UTF-8") as f:
    data = np.array([list(x.strip()) for x in f.readlines()], dtype=int)

# calculate the forward difference along rows
d_row_fwd = np.zeros_like(data)
d_row_fwd[:-1, :] = data[1:, :] - data[:-1, :]

d_row_back = np.zeros_like(data)
d_row_back[1:, :] = -d_row_fwd[:-1, :]

d_col_fwd = np.zeros_like(data)
d_col_fwd[:, :-1] = data[:, 1:] - data[:, :-1]

d_col_back = np.zeros_like(data)
d_col_back[:, 1:] = -d_col_fwd[:, :-1]

directions = np.array([[1, 0], [-1, 0], [0, 1], [0, -1]])

allowed_steps = np.array(
    [d_row_fwd == 1, d_row_back == 1, d_col_fwd == 1, d_col_back == 1]
)

# get all trail head positions
trail_head_coords = np.array(np.where(data == 0)).T

total = 0

for i_th, coord in enumerate(trail_head_coords):
    G = nx.DiGraph()
    height = 0

    start_c = coord
    c = coord
    possible_dirs = directions[np.where(allowed_steps[:, c[0], c[1]])[0]]

    # update coord
    new_coords = c + possible_dirs

    for nc in new_coords:
        G.add_edge(tuple(c), tuple(nc))

    coord = new_coords
    height += 1  # = 1

    while height < 9:
        new_coords = []
        for c in coord:
            possible_dirs = directions[np.where(allowed_steps[:, c[0], c[1]])[0]]
            tmp = c + possible_dirs

            for nc in tmp:
                G.add_edge(tuple(c), tuple(nc))

            new_coords.append(tmp)

        coord = np.unique(np.vstack(new_coords), axis=0)
        height += 1  # = 2

    num_trails = sum(
        [
            len(list(nx.all_simple_paths(G, source=tuple(start_c), target=tuple(x))))
            for x in coord
        ]
    )

    print(i_th, start_c, num_trails)

    total += num_trails

    if num_trails == 46:
        plt.figure(figsize=(8, 6))
        nx.draw(
            G,
            with_labels=True,
            node_color="lightblue",
            node_size=20,
            font_size=5,
            font_color="black",
            edge_color="gray",
            arrowsize=5,
        )
        plt.title("Graph Visualization")
        plt.show()


print(total)
