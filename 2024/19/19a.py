import re

test = True

if test:
    substring_file = "substrings_test.txt"
    input_file = "input_test.txt"
else:
    substring_file = "substrings.txt"
    input_file = "input.txt"


# Read the substrings from the file
with open(substring_file, "r", encoding="UTF-8") as file:
    line = file.readline().strip()  # Read the single line and strip whitespace

# Split the substrings by the delimiter (comma and optional spaces)
substrings = [s.strip() for s in line.split(",")]

# Create the regex pattern dynamically
pattern = f"^({'|'.join(map(re.escape, substrings))})+$"

# Read the test strings from the file
with open(input_file, "r", encoding="UTF-8") as f:
    test_strings = [line.strip() for line in f]

# Check each string
counter = 0

for string in test_strings:
    if re.fullmatch(pattern, string):
        counter += 1
    # else:
    #    print(f"'{string}' does not match the pattern.")

print(f"counter: {counter}")
