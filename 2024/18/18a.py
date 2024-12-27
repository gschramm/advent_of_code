import networkx as nx
import matplotlib.pyplot as plt

plot_graph = True
test = False


# read input_test.txt which which is a 2 column csv file containing integers
# into a list of tuples containing 2 ints
if test:
    n = 7
    n_first_bytes = 12
    with open("input_test.txt", "r", encoding="UTF-8") as f:
        nodes_to_remove = [tuple(map(int, line.split(","))) for line in f]
else:
    n = 71
    n_first_bytes = 1024
    with open("input.txt", "r", encoding="UTF-8") as f:
        nodes_to_remove = [tuple(map(int, line.split(","))) for line in f]

# add nodes (0,0), (0,1), ... (1,0) ... (n-1,n-1) to the graph
G = nx.grid_2d_graph(n, n)

for node in nodes_to_remove[:n_first_bytes]:
    G.remove_node(node)

# find the shortest path from (0,0) to (n-1,n-1)
shortest_path = nx.shortest_path(G, (0, 0), (n - 1, n - 1))

print(len(shortest_path) - 1)

# visualize the graph
if plot_graph:
    nx.draw(G, with_labels=True)
    plt.show()
