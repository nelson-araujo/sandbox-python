# Bill spliter calculator
# Use tipe %: 10, 12, or 15
# Calculate how much each person in the group owes

# Pseudocode
# bill <- "What was the total bill?"
# tip = -1
# while tip != 10, 12, or 15
#   tip <- "How much would you like to tip? Must be 10,12,15?"
# guests = -1
# while guests != >0
#   guests <- "How many guests to split the bill with?"
# bill_total = bill * (1+(tip/100))
# owed_per_guest = round(bill_total / guests, 2)
# "Each guests owes ${owed_per_guests}.}"

print(f"Welcome to the Bill Splitter Calculator")

# Get bill ammount
bill = float( input("What is the total bill? ") )

# Get ammount to tip
tip = -1
while tip!=10 and tip!=12 and tip!=15:
    tip = float(input(f"How much would you like to tip? Must be 10,12, or 15: "))

# Get number of guests
guests = -1
while guests <1:
    guests = int( input("How many guests to split the bill with? ") )

# Calculate total bill
bill_total = round(bill * (1+tip/100),2)

# Calculate per guest
bill_per_person = round(bill_total / guests, 2)


# Display breakdown
print(f"\nWith a bill of ${bill:.2f} and a tip of {int(tip)}% the total bill is ${bill_total:.2f}.")
print(f"Spliting the total bill between {guests} people; each person owes ${bill_per_person:.2f}.")