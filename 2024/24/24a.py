import networkx as nx
from functools import cache

with open("gates.txt", "r", encoding="UTF-8") as f:
    lines = [x.strip().split(" ") for x in f.read().splitlines()]

with open("init.txt", "r", encoding="UTF-8") as f:
    init = [x.strip().split(": ") for x in f.read().splitlines()]

wire_lut = dict()
for i in init:
    wire_lut[i[0]] = int(i[1])

G = nx.DiGraph()
op_lut = dict()

for line in lines:
    G.add_edge(line[0], line[-1], label=line[1])
    G.add_edge(line[2], line[-1], label=line[1])
    op_lut[line[-1]] = line[1]


# %%
@cache
def process(node):
    preds = list(G.predecessors(node))

    if len(preds) == 0:
        return wire_lut[node]
    else:
        op = op_lut[node]
        if op == "AND":
            return process(preds[0]) & process(preds[1])
        elif op == "OR":
            return process(preds[0]) | process(preds[1])
        elif op == "XOR":
            return process(preds[0]) ^ process(preds[1])
        else:
            raise ValueError("Unknown operation")


# %%
z_nodes = sorted([x for x in G.nodes if x.startswith("z")])

total = 0

for i, node in enumerate(z_nodes):
    print(node, process(node))
    total += process(node) * (2**i)

print()
print(total)

# %%
import matplotlib.pyplot as plt
from networkx.drawing.nx_agraph import graphviz_layout

fig, ax = plt.subplots(figsize=(25, 25))
pos = graphviz_layout(
    G, prog="dot", args="-Grankdir=TB"
)  # Use the dot layout for layering
nx.draw(
    G,
    pos,
    ax=ax,
    with_labels=True,
    node_size=100,
    node_color="lightblue",
    arrowsize=5,
    font_size=3,
)
nx.draw_networkx_edge_labels(
    G, pos, edge_labels=nx.get_edge_attributes(G, "label"), font_size=1
)
fig.savefig("graph.png", dpi=600)
