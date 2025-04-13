
from random import sample

# Initiate an empty 9x9 grid
grid = []

# Generate rows with unique numbers (1 to 9) using random.sample()
while len(grid) < 9:
    new_row = sample(range(1, 10), 9)  # Random row with unique numbers
    valid = True
    
    # Check if new_row is valid in terms of column uniqueness
    for col in range(9):
        col_vals = [grid[r][col] for r in range(len(grid))]  # Collect existing values in this column
        if new_row[col] in col_vals:
            valid = False
            break
    
    # Only add new_row if it's valid (no column conflicts)
    if valid:
        grid.append(new_row)

# Print the final 9x9 grid
for row in grid:
    print(row)