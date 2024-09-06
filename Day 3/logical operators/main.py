# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

concat_names = name1 + name2
lower_concat_name = concat_names.lower()

t = lower_concat_name.count("t")
r = lower_concat_name.count("r")
u = lower_concat_name.count("u")
e = lower_concat_name.count("e")

count_true = t + r + u + e


l = lower_concat_name.count("l")
o = lower_concat_name.count("o")
v = lower_concat_name.count("v")
e = lower_concat_name.count("e")

count_love = l + o + v + e

love_count = str(count_true) + str(count_love)

if int(love_count) < 10 or int(love_count) > 90:
    print(f"Your score is {love_count}, you go together like coke and mentos.")
elif int(love_count) > 40 and int(love_count) < 50:
    print(f"Your score is {love_count}, you are alright together.")
else:
    print(f"Your score is {love_count}.")