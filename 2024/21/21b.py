from functools import cache
from collections import Counter

# move priority: <, ^, v, >

#     +---+---+
#     | ^ | A |
# +---+---+---+
# | < | v | > |
# +---+---+---+


# |A| <vA <A A >>^A vA A <^A >A | <v<A >>^A vA ^A | <vA >^A <v<A >^A >A A vA ^A | <v<A >A >^A A A vA <^A >A
# |A| v<<A >>^A                 | <A >A           | vA <^A A >A                 | <vA A A >^A
# |A| <A                        | ^A              | >^^A                        | vvvA
# |A| 029A

arrow_cache = {}

# get all the moves starting at "A"
arrow_cache[("A", "A")] = "A"
arrow_cache[("A", "<")] = "v<<A"  # only possible move without zigzag
arrow_cache[("A", "v")] = "<vA"
arrow_cache[("A", "^")] = "<A"
arrow_cache[("A", ">")] = "vA"

# get all the moves starting at "^"
arrow_cache[("^", "^")] = "A"
arrow_cache[("^", "A")] = ">A"
arrow_cache[("^", "v")] = "vA"
arrow_cache[("^", "<")] = "v<A"  # only move
arrow_cache[("^", ">")] = "v>A"
### unsure two options "v>A" or ">vA" (probably the first)

# get all the moves starting at ">"
arrow_cache[(">", ">")] = "A"
arrow_cache[(">", "A")] = "^A"
arrow_cache[(">", "v")] = "<A"
arrow_cache[(">", "<")] = "<<A"
arrow_cache[(">", "^")] = "<^A"  # from example

# get all the moves starting at "v"
arrow_cache[("v", "v")] = "A"
arrow_cache[("v", ">")] = ">A"
arrow_cache[("v", "<")] = "<A"
arrow_cache[("v", "^")] = "^A"
arrow_cache[("v", "A")] = "^>A"  # from example (reversed for 25)

# get all the moves starting at "<"
arrow_cache[("<", "<")] = "A"
arrow_cache[("<", "v")] = ">A"
arrow_cache[("<", ">")] = ">>A"
arrow_cache[("<", "^")] = ">^A"  # only possible move
arrow_cache[("<", "A")] = ">>^A"  # avoid zig zag, but example has it :/


# %%
@cache
def process_str(input_str: str) -> list[str]:
    output = [arrow_cache[("A", input_str[0])]]

    for i in range(len(input_str) - 1):
        output.append(arrow_cache[(input_str[i], input_str[i + 1])])

    return output


# %%

# +---+---+---+
# | 7 | 8 | 9 |
# +---+---+---+
# | 4 | 5 | 6 |
# +---+---+---+
# | 1 | 2 | 3 |
# +---+---+---+
#     | 0 | A |
#     +---+---+

test = False
num_arrow_robs = 25

if test:
    inputs = [
        ("029A", ["<A", "^A", ">^^A", "vvvA"]),
        ("980A", ["^^^A", "<A", "vvvA", ">A"]),
        ("179A", ["^<<A", "^^A", ">>A", "vvvA"]),
        ("456A", ["^^<<A", ">A", ">A", "vvA"]),
        ("379A", ["^A", "<<^^A", ">>A", "vvvA"]),
    ]
else:
    inputs = [
        ("869A", ["<^^^A", "v>A", "^A", "vvvA"]),  # 8 to 6 unclear
        ("180A", ["^<<A", "^^>A", "vvvA", ">A"]),  # 1 to 8 unclear
        ("596A", ["<^^A", "^>A", "vA", "vvA"]),  # 5 to 9 unclear
        ("965A", ["^^^A", "vA", "<A", "vv>A"]),  # 5 to A unclear
        ("973A", ["^^^A", "<<A", "vv>>A", "vA"]),  # 7 to to 3 unclear
    ]


## %%
total = 0

for inp in inputs:
    code = inp[0]
    num_val = int(code[:3])

    counter = Counter(inp[1])

    for j in range(num_arrow_robs):
        new_counter = Counter()
        for key, counts in counter.items():
            for out in process_str(key):
                new_counter[out] += counts

        counter = new_counter

    # sum of the number of chars
    num_chars = 0
    for key, counts in counter.items():
        num_chars += len(key) * counts

    print(code, num_chars)

    # increase the total
    total += num_chars * num_val

print()
print(total)
print(total / 1e13)
