import networkx as nx
from functools import cache

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
# create a look up table for the outputs of the upper L gates

upper_gate_lut_p = dict()
upper_gate_lut_q = dict()

for i in range(1, 45):
    upper_gate_lut_p[gates[(f"x{i:02}", f"y{i:02}", "XOR")]] = f"p{i:02}"
    upper_gate_lut_q[gates[(f"x{i:02}", f"y{i:02}", "AND")]] = f"q{i:02}"

########################################################################
# upper L gate 37 (x37,y37) input has wrong q (AND) output (z37)
########################################################################

# loop over all lower L gates that take p as input
lower_gate_lut_z = dict()
lower_gate_lut_d = dict()

for code, pval in upper_gate_lut_p.items():
    # print(code, pval)
    try:
        lower_gate_lut_z[pval] = [
            value
            for key, value in gates.items()
            if (key[0] == code or key[1] == code) and key[2] == "XOR"
        ][0]
    except:
        print("z error", code, pval)

    try:
        lower_gate_lut_d[pval] = [
            value
            for key, value in gates.items()
            if (key[0] == code or key[1] == code) and key[2] == "AND"
        ][0]
    except:
        print("d error", code, pval)

########################################################################
# p37 ("vvm") should be connected a lower L gate (two nodes), but is only connected to node "wrd" (OR)
########################################################################

# %%
# check the OR gates based on upper gate q lookup and lower gate d lut
