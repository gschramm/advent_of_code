import networkx as nx

with open("input.txt", "r", encoding="UTF-8") as f:
    connections = [x.strip().split("-") for x in f.readlines()]

G = nx.Graph()

for connection in connections:
    G.add_edge(connection[0], connection[1])

# Find all maximal cliques
cliques = list(nx.find_cliques(G))

# Find the largest clique
largest_clique = max(cliques, key=len)

print("Size of the largest clique:", len(largest_clique))
print("Largest clique:", largest_clique)
print()
print(",".join(sorted(largest_clique)))
