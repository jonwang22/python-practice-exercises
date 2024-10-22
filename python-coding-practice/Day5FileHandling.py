# Write a Python script that reads from a text file named data.txt and prints each line with its line number. Test Script by creating a data.txt file

# Output Example: (data.txt contains:)

# Hello, world!

# Opening file "data.txt" in read mode
file = open("/home/ubuntu/python-practice-exercises/data.txt", "r")

# initializing line number counter
line_number = 1

# printing each line in file, with line number
for line in file:
    print(f"{line_number} {line}")
    line_number += 1