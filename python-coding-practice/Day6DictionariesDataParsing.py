# Write a Python script that creates a dictionary to store information about three students (name, age, and grade) and prints each student's information in a readable format. Test Script: Include a sample dictionary in your script.

# Output Example:

# Name: John, Age: 20, Grade: A Name: Jane, Age: 22, Grade: B Name: Alice, Age: 19, Grade: A

# Creating Lists for name, age, grade
name = ["John", "Jane", "Alice"]
age = [20, 22, 19]
grade = ["A", "B", "A"]

# Creating dictionary
dict = {
    "Name": name,
    "Age": age,
    "Grade": grade,
}

length = len(dict)
empty = ""

for i in range(length):
    for key, value in dict.items():
        if i == length-1:
            var = f"{key.title()}: {value[i]} "
        else:
            var = f"{key.title()}: {value[i]}, "
        empty += var

print(empty)