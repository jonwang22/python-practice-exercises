# Write a Python function fahrenheit_to_celsius(fahrenheit) that converts a temperature from Fahrenheit to Celsius. The script should prompt the user for a temperature in Fahrenheit, use the function to convert it and print the result.

# Output Example: 

# Enter temperature in Fahrenheit: 98.6
# 98.6 Fahrenheit is 37.0 Celsius

# Defining functions
def fahrenheit_to_celsius(degree):
    celsius = (degree - 32) * 5/9
    print(f"{degree} Fahrenheit is {celsius:.1f} Celsius")
    return celsius

def celsius_to_fahrenheit(degree):
    fahrenheit = (degree * 9/5) + 32
    print(f"{degree} Celsius is {fahrenheit:.1f} Fahrenheit")
    return fahrenheit

# User determines temp unit
temp_unit = input("What unit of temperature do you want to use(Fahrenheit or Celsius)? ")

# If conditionals comparing user input if it matches expected unit of measurement.
if temp_unit.lower() in ["fahrenheit", "f"]:
    degree_temp = float(input("Enter temp to convert: "))
    fahrenheit_to_celsius(degree_temp)
elif temp_unit.lower() in ["celsius", "c"]:
    degree_temp = float(input("Enter temp to convert: "))
    celsius_to_fahrenheit(degree_temp)
else:
    print("Please select a proper temp unit.")