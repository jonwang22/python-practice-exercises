coffee = ["Café Latte", "Caffe Americano", "Espresso", "Cappuccino", "Macchiato"]

choice = int(input("Please select your beverage: "))

try:
	#your code goes here
	print("Here is your "+coffee[int(choice)])
except (ValueError, IndexError):
	#and here
	print("Invalid number")
finally:
	#and finally here
	print("Have a good day")