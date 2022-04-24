h=float(input("Height [m]: "))
w=int(input("Weight [kg]: "))

bmi=w/(h*h)

if bmi<18.5:
    print("Underweight")
elif bmi>=18.5 and bmi<25:
    print("Normal")
elif bmi>=25 and bmi<30:
    print("Overweight")
else:
    print("Obese")
