"""
Program: Meal Price Calculator
Author: Sairi Conejo Flores

Purpose: Calculate the total price of the meal with different prices.
"""

# One more option has been added to the calculator that can be used
# to include the tip or not.
# This is a conditional that the user may or may not reject.
# Added a function to prevent a value from being less than or equal to 0
# and another to prevent the payment from being less than the total.

def get_value(message,type):
    while True:
        value = input(message)

        if type == "float":
            value = float(value)
            if value > 0:
                break
            else:
                print("\nPlease, enter a value greater than 0.")
        elif type == "int":
            value = int(value)
            if value > 0:
                break
            else:
                print("\nPlease, enter a value greater than 0.")

    return value

print("Please enter the following.")

child_price = get_value("What is the price of a child's meal?: ", "float")
adult_price = get_value("What is the price of an adult's meal?: ", "float")
num_children = get_value("How many children are there?: ", "int")
num_adults = get_value("How many adults are there?: ", "int")

# Subtotal before tax
subtotal = (child_price * num_children) + (adult_price * num_adults)
print(f"Subtotal: ${subtotal:.2f}")

# Tax calculation
tax_rate = get_value("What is the sales tax rate?: ", "float")
sales_tax = (subtotal * tax_rate) / 100
print(f"Sales Tax: ${sales_tax:.2f}")

# Total included with taxes
total = subtotal + sales_tax
print(f"Total: ${total:.2f}")

# Amount received from the user
def get_payment(message):
    while True:
        value  = float(input(message))

        if value >= total:
            break
        else:
            print("The amount entered is less than your total payment.")
        
    return value

payment = get_payment("What is the payment amount?: ")

# tips
# min_tip = (total * 1) / 100 # The minimum percentage is 1
if payment > total + 0.5: # Simplified tip logic with a minimum threshold
    tip_choice = (input("Would you like to add a tip? (y/n): ")).lower()

    if tip_choice == 'y':
        tip_percentage = get_value("What is the tip percentage?: ", "float")
        tip = (total * tip_percentage) / 100
        total += tip
    else:
        pass

change = payment - total
print(f"Change: ${change:.2f}")