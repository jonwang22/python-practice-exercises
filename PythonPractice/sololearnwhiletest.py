total = 0
passengers = 5
age = 0
while passengers > 0:
    age = int(input("Please input an age: "))
    if age >= 3:
        total += 100
        # print(total)
        passengers -= 1
    elif age < 3:
        passengers -= 1
        print("Passenger is under 3 years old, ticket is free")
        continue

print (total)