import re

# read file into a single line and remove line breaks
# also add a do() and don't() at the beginning and end of the line
with open("input.txt", "r", encoding="UTF-8") as f:
    text = "do()" + "".join([l.strip() for l in f.readlines()]) + "don't"

# we extract all substring surrounded by do() and don't() and process them 1 by 1
# we need to add the "?" to make sure we use the non-greedy version of the regex
total = 0
for substr in re.findall(r"do\(\)(.+?)don't\(\)", text):
    total += sum(
        [int(m[0]) * int(m[1]) for m in re.findall(r"mul\((\d+),(\d+)\)", substr)]
    )

print(total)
