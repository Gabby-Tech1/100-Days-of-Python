# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# BMI = int(weight) / (int(height) ** 2)
# print(BMI)

actual_height = float(height)
actual_weight = float(weight)

BMI = actual_weight / (actual_height ** 2)
round_BMI = int(BMI)
print(round_BMI)