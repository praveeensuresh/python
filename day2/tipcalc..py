print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
total_bill=(bill*(1+tip/100))
split=total_bill/5
print(f"total bill={round(total_bill,2)} split={round(split,2)}")