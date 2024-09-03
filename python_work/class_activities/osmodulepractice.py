import os

# Create a Python script that counts the number of items (files and directories) in a specified directory(take dir as input). 
# The script should display the total number of items (both files and directories) present in the specified directory. 
# Bonus Modify your script to count the number of files and directories separately. Hint: use the os module

directory = input("What directory do you want to check? \n")
count = 0

directory_list = os.listdir(directory)

print(f"Files and Directories in {directory}.")
print(directory_list)
print(type(directory_list))

for item in directory_list:
    count += 1
    
print(f"Items in directory: {count}")


# Challenge
file_count = 0
dir_count = 0
for item in directory_list:
    if os.path.isfile(os.path.join(directory, item)):
        file_count += 1
    elif os.path.isdir(os.path.join(directory, item)):
        dir_count += 1
    else:
        print("what")
print(f"File count: {file_count}")
print(f"Directory count: {dir_count}")
