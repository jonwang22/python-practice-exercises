file = open("books.txt", "r")

#your code goes here
contents = file.readlines()

for i in contents:
    if '\n' in i:
        print(i[0] + str(len(i) - 1))
    else:
        print(i[0] + str(len(i)))

file.close()