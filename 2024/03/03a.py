import re

with open("input.txt") as f:
    lines = f.readlines()

# concatenate all lines but remove the newline characters
line = "".join([l.strip() for l in lines])

total = 0

pattern = r"mul\((\d+),(\d+)\)"
for match in re.findall(pattern, line):
    total += int(match[0]) * int(match[1])

print(total)
