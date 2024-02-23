weight = float(input("Input your weight here (in kilograms): "))
height = float(input("Input your height here (in meters): "))
BMI = weight/height**2

if BMI < 18.5:
    print("Your BMI is ",BMI)
    print("Underweight")
elif BMI >= 18.5 and BMI < 25:
    print("Your BMI is ",BMI)
    print("Normal")
elif BMI >= 25 and BMI < 30:
    print("Your BMI is ",BMI)
    print("Overweight")
elif BMI > 30:
    print("Your BMI is ",BMI)
    print("Obesity")
