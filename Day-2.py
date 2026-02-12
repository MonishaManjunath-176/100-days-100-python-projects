print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))
total_tip = bill * tip / 100
bill_with_tip = bill + total_tip
print("each person should pay:" + str(bill_with_tip/ people))
