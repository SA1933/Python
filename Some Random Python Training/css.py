import itertools

# Generate all combinations of 5-digit passwords using digits 0-9
digits = '0123456789'
combinations = list(itertools.product(digits, repeat=5))

# Generate CSS styles
css_styles = []
for combo in combinations:
    hex_color = f"#{''.join(combo[:2])}{''.join(combo[2:4])}{''.join(combo[4:])}"
    css_styles.append(f".color-{''.join(combo)} {{ background-color: '{hex_color}'; }}")

# Save CSS styles to a .txt file
with open('css_combinations.txt', 'w') as file:
    file.write("\n".join(css_styles))

print("CSS styles have been saved to css_combinations.txt")
