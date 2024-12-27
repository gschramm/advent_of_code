import re
from functools import cache


def count_combinations(substrings, target):
    # Convert substrings to a set for fast lookup
    substrings = set(substrings)

    @cache
    def helper(index):
        # If we reached the end of the string, it's a valid combination
        if index == len(target):
            return 1

        count = 0
        # Try every possible substring starting from the current index
        for substring in substrings:
            if target.startswith(substring, index):
                count += helper(index + len(substring))

        return count

    # Start recursion from index 0
    return helper(0)


if __name__ == "__main__":
    test = False

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
    substrs = [s.strip() for s in line.split(",")]

    # Create the regex pattern dynamically
    pattern = f"^({'|'.join(map(re.escape, substrs))})+$"

    # Read the test strings from the file
    with open(input_file, "r", encoding="UTF-8") as f:
        test_strings = [line.strip() for line in f]

    # Check each string
    counter = 0

    for string in test_strings:
        if re.fullmatch(pattern, string):
            counter += count_combinations(substrs, string)
        # else:
        #    print(f"'{string}' does not match the pattern.")

    print(f"counter: {counter}")
