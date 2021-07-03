print("Enter the weight(in kg)")
w = float(input())
# Adwaith-4-BMI
print("Enter the height(in m)")
h = float(input())

# read height and weight

BMI = ((w) / (h**2))

# calculates BIM 

rBMI = round(BMI, 2)

# round the value of BMI upto 2 digits after decimal

print("The BMI is", rBMI)

# Conditions given in question


if rBMI < 18.5:
	print("You are Underweight")
elif rBMI > 18.5 and rBMI < 25:
	print("You are Normalweight")
elif rBMI > 25 and rBMI < 30:
	print("You are overweight")
elif rBMI > 30 and rBMI < 35:
	print("You are obese")
elif rBMI > 35:
	print("You are clinically obese")
