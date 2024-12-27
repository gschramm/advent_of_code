from sympy import symbols, Eq, solve
import re
import pandas as pd

# %%
# parse input


# Read the file
with open("input.txt", "r", encoding="UTF-8") as file:
    data = file.read()

# Define a regular expression pattern to extract the required fields
pattern = r"Button A: X\+(\d+), Y\+(\d+)\nButton B: X\+(\d+), Y\+(\d+)\nPrize: X=(\d+), Y=(\d+)"

# Find all matches
matches = re.findall(pattern, data)

# Convert matches to a structured format (list of dictionaries or DataFrame)
parsed_data = [
    {
        "Button A X": int(match[0]),
        "Button A Y": int(match[1]),
        "Button B X": int(match[2]),
        "Button B Y": int(match[3]),
        "Prize X": int(match[4]),
        "Prize Y": int(match[5]),
    }
    for match in matches
]

# Convert to a pandas DataFrame for better handling
df = pd.DataFrame(parsed_data)

# Define the equations
# eq1 = Eq(94 * x + 22 * y, 8400)
# eq2 = Eq(34 * x + 67 * y, 5400)

# eq1 = Eq(26 * x + 67 * y, 12748)
# eq2 = Eq(66 * x + 21 * y, 12176)

# eq1 = Eq(17 * x + 84 * y, 7870)
# eq2 = Eq(86 * x + 37 * y, 6450)

total_price = 0

# %%
# iterate over the rows of df
for i_row, row in df.iterrows():
    x, y = symbols("x y")
    # Define the equations
    eq1 = Eq(row["Button A X"] * x + row["Button B X"] * y, row["Prize X"])
    eq2 = Eq(row["Button A Y"] * x + row["Button B Y"] * y, row["Prize Y"])

    # Solve the first equation for y in terms of x
    y_solution = solve(eq1, y)[0]

    # Substitute y into the second equation
    eq2_substituted = eq2.subs(y, y_solution)

    # Solve for x (integer solutions)
    x_solution = solve(eq2_substituted, x)

    # Use x to find corresponding y values
    y_values = [y_solution.subs(x, xi) for xi in x_solution]

    # Print solutions
    for i, x_sol in enumerate(x_solution):
        y_sol = y_values[i]
        if x_sol.is_integer and y_sol.is_integer:
            if x_sol >= 0 and y_sol >= 0:
                price = 3 * x_sol + 1 * y_sol
                total_price += price
                print(i_row, i, x_sol, y_sol, price)


print(total_price)
