# Create a list of the first 10 numbers and write a script that prints each number multiplied by 2.

# Output Example: 

# 0 * 2 = 0
# 1 * 2 = 2
# 2 * 2 = 4
# 3 * 2 = 6
# 4 * 2 = 8
# 5 * 2 = 10
# 6 * 2 = 12
# 7 * 2 = 14
# 8 * 2 = 16
# 9 * 2 = 18

# List of first 10 numbers
list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# iterate through list and multiply number by 2
for number in list:
    product = number * 2
    print(f"{number} * 2 = {product}")