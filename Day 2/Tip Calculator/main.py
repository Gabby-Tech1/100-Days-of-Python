print("Welcome to the tip calculator.")

total_bill = float(input("What was the total bill? "))
percentage = float(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

percentage_bill = (percentage / 100) * total_bill
total_bill += percentage_bill

bill_for_each = total_bill / people
result = round(bill_for_each, 2)

print(f"Each person should pay: {result}")