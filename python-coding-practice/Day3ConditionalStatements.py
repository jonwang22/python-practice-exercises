# Write a Python script that takes a number as input and prints whether it is odd or even.

# Output Example:

# Enter a number: 7
# 7 is odd

# Take user input converting to integer
user_input = int(input("Enter a number: "))

# If number divisible by 2 then even, else odd.
if user_input % 2 == 0:
    print(f"{user_input} is even.")
else:
    print(f"{user_input} is odd.")