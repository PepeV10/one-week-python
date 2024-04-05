# Prompting the user for input
height = float(input("Enter your height in inches: "))
weight = float(input("Enter your weight in pounds: "))

# Calculating BMI
bmi = (weight * 703) / (height ** 2)

# Outputting the BMI and category
print(f"Your BMI is {bmi:.2f}")

if bmi < 16.0:
    print("You are Severely Underweight")
elif bmi <= 18.4:
    print("You are Underweight")
elif bmi <= 24.9:
    print("Your weight is Normal")
elif bmi <= 29.9:
    print("You are Overweight")
elif bmi <= 34.9:
    print("You are Moderately Obese")
elif bmi <= 39.9:
    print("You are Severely Obese")
else:
    print("You are Morbidly Obese")

"""
# Colt's Solution
# Prompting the user for input
height = float(input("What is your height in (in inches): "))
weight = float(input("What is your weight in (lbs pounds): "))

# Calculating BMI
bmi = (weight * 703) / (height ** 2)

# Outputting the BMI and category
bmi = round(bmi, 1)

if bmi < 16.0:
    category = "Severely Underweight"
elif bmi <= 18.4:
    category = "Underweight"
elif bmi <= 24.9:
    category = "Normal"
elif bmi <= 29.9:
    category = "Overweight"
elif bmi <= 34.9:
    category = "Moderately Obese"
elif bmi <= 39.9:
    category = "Severely Obese"
else:
    category = "Morbidly Obese"

print(f"Your BMI of {bmi} makes you {category}")
"""