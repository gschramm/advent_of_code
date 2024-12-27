import networkx as nx
from functools import cache


class LUT:
    def __init__(self):
        self.forward = {}  # Key-to-Value
        self.reverse = {}  # Value-to-Key

    def add(self, key, value):
        if key in self.forward or value in self.reverse:
            raise ValueError("Duplicate key or value detected!")
        self.forward[key] = value
        self.reverse[value] = key

    def get_by_key(self, key):
        return self.forward.get(key)

    def get_by_value(self, value):
        return self.reverse.get(value)


with open("gates.txt", "r", encoding="UTF-8") as f:
    lines = [x.strip().split(" ") for x in f.read().splitlines()]

with open("init.txt", "r", encoding="UTF-8") as f:
    init = [x.strip().split(": ") for x in f.read().splitlines()]


gates = {}

for line in lines:
    out = line[-1]
    op = line[1]
    tmp = sorted([line[0], line[2]])
    gates[(tmp[0], tmp[1], op)] = out

# %%
G = nx.DiGraph()
op_lut = dict()

for line in lines:
    G.add_edge(line[0], line[-1], label=line[1])
    G.add_edge(line[2], line[-1], label=line[1])
    op_lut[line[-1]] = line[1]


# %%
# create a look up table for the outputs of the upper L gates

upper_gate_lut_p = LUT()
upper_gate_lut_q = LUT()

for i in range(1, 45):
    upper_gate_lut_p.add(gates[(f"x{i:02}", f"y{i:02}", "XOR")], f"p{i:02}")
    upper_gate_lut_q.add(gates[(f"x{i:02}", f"y{i:02}", "AND")], f"q{i:02}")

########################################################################
# upper L gate 37 (x37,y37) input has wrong q (AND) output (z37)
########################################################################

# loop over all lower L gates that take p as input
lower_gate_lut_z = LUT()
lower_gate_lut_d = LUT()

for code, pval in upper_gate_lut_p.forward.items():
    # print(code, pval)
    try:
        lower_gate_lut_z.add(
            pval,
            [
                value
                for key, value in gates.items()
                if (key[0] == code or key[1] == code) and key[2] == "XOR"
            ][0],
        )
    except:
        print("z error", code, pval)

    try:
        lower_gate_lut_d.add(
            pval,
            [
                value
                for key, value in gates.items()
                if (key[0] == code or key[1] == code) and key[2] == "AND"
            ][0],
        )
    except:
        print("d error", code, pval)

########################################################################
# p33 ("vvm") should be connected to a lower L gate (two nodes), but is only connected to node "wrd" (OR)
########################################################################

# %%
# check the OR gates based on upper gate q lookup and lower gate d lut

for i in range(1, 45):
    try:
        or_inp1 = upper_gate_lut_q.reverse[f"q{i:02}"]
        or_inp2 = lower_gate_lut_d.forward[f"p{i:02}"]

        n = 0

        try:
            or_gate = gates[(or_inp1, or_inp2, "OR")]
            n += 1
        except KeyError:
            pass

        try:
            or_gate = gates[(or_inp2, or_inp1, "OR")]
            n += 1
        except KeyError:
            pass

        if n == 2:
            print(f"2 OR gates for: {i:02}")
        if or_gate.startswith("z"):
            print(f"OR gate z output for: {i:02}, {or_inp1}, {or_inp2}")

    except:
        print(f"OR error: {i:02}")

########################################################################
# z12 is an output of the OR gate (fsf, nqs), but should be output of lower L gate
########################################################################

for i in range(45):
    op = op_lut[f"z{i:02}"]
    if op != "XOR":
        print(i, "z op error")


# %%
# swap output was obtained by looking at the graph visualized in (part a)

swap_output = ["fgc", "z12", "vvm", "dgr", "z37", "dtv", "mtj", "z29"]

print(",".join(sorted(swap_output)))
