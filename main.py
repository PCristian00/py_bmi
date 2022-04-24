w = int(input("Weight [kg]: "))
h = float(input("Height [m]: "))

bmi = w / (h * h)

if bmi < 18.5:
    print("Underweight")
elif bmi >= 18.5 and bmi < 25:
    print("Normal")
elif bmi >= 25 and bmi < 30:
    print("Overweight")
else:
    print("Obesity")
