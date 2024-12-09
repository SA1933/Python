import itertools

# Generate all combinations of 5-digit passwords using digits 0-9
digits = '0123456789'
combinations = list(itertools.product(digits, repeat=5))

# Set the number of combinations to display per row
combinations_per_row = 10

# Display combinations in a table format
print("Tabel Kombinasi Password 5 Digit:")
print("-" * 50)  # Header line
print("No  | Kombinasi")
print("-" * 50)  # Separator

for index, combo in enumerate(combinations):
    if index % combinations_per_row == 0 and index != 0:
        print("")  # Print a new line after each row

    # Print the index (No) and the combination
    print(f"{index + 1:<3} | {''.join(combo)}")

print("-" * 50)  # Footer line
print(f"Total kombinasi: {len(combinations)}")
