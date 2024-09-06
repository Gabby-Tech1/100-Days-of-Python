# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


BMI = weight / (height ** 2)
rounded_BMI = round(BMI)

if rounded_BMI < 18.5:
    print(f"Your BMI is {rounded_BMI}, you are underweight.")
elif rounded_BMI < 25:
    print(f"Your BMI is {rounded_BMI}, you have a normal weight.")
elif rounded_BMI < 30:
    print(f"Your BMI is {rounded_BMI}, you are slightly overweight.")
elif rounded_BMI < 35:
    print(f"Your BMI is {rounded_BMI}, you are obese.")
else:
    print(f"Your BMI is {rounded_BMI}, you are clinically obese")