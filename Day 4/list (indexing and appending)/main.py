# Split string method
import random


names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

chosen_name_index = random.randint(0, len(names)-1)
chosen_name = names[chosen_name_index]
print(f"{chosen_name} is going to buy the meal today!")
