import networkx as nx

with open("input.txt", "r", encoding="UTF-8") as f:
    connections = [x.strip().split("-") for x in f.readlines()]

G = nx.Graph()

for connection in connections:
    G.add_edge(connection[0], connection[1])

triplets = [clique for clique in nx.enumerate_all_cliques(G) if len(clique) == 3]

total = 0

for triplet in triplets:
    # print(triplet)
    if any([x.startswith("t") for x in triplet]):
        total += 1

print("total", total)
