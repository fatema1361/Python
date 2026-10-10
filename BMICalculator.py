print("BMI Calculator!")

weight=float(input("Enter your weight in kilogram: "))
height=float(input("Enter your hieght in meters: "))
bmi=weight/(height**2)
print("Your BMI is : ",bmi)
if bmi<18.5:
    print("UnderWeight")
elif bmi>=18.5 and bmi<24.9:
    print("Normal weight")
elif bmi>=25 and bmi<29.9:
    print("Overweight")
elif bmi>=30 and bmi<39.9:
    print("Obesity")
elif bmi>=40:
    print("Extreme Obesity")


