"""
Program: Shopping Cart
Author: Sairi Conejo Flores

Purpose: List exercise: Shopping cart with user interactions
"""
# The entire program is worked with functions
# Added some data type validations


def menu():
    print("""
Please select one of the following:
1 Add item
2 View cart
3 Remove item
4 Compute total
5 Quit
""")
    

def add_item(items, prices):
    item = input("What item would you like to add?: ")
    while len(item) <= 2:
        print("\nThe item must be at least 3 characters.")
        item = input("What item would you like to add?: ")

    while True:
        price = input(f"What is the price of '{item}'?: ")
        if price.strip() == "":
            print("\nThe price cannot be empty. Please enter a valid price.")
        else:
            price = float(price)
            if price <= 0:
                print("\nYou have entered a negative or zero value. Try again.")
            else:
                break # if the conversion is successful exit the loop

    items.append(item)
    prices.append(float(price))
    print(f"\n'{item}' has been added to the cart.")


def remove_item(items, prices):
    if len(items) > 0:
        view_cart(items, prices) # show the shopping cart again

        while True:
            item_to_remove = input("Which item would you like to remove?: ")

            if item_to_remove.isdigit():
                item_to_remove = int(item_to_remove)
                if 1 <= item_to_remove <= len(items):
                    item_to_remove -= 1 # convert to zero based index
                    items.pop(item_to_remove)
                    prices.pop(item_to_remove)
                    print("\nItem removed")
                    break
                else:
                    print("\nInvalid item number. Please select a valid item number.")
            else:
                print("\nPlease enter a valid number.")
    else:
        print("\nYour cart is empty.")


def total(prices):
    total = 0
    for price in prices:
        total += price
    
    print(f"\nThe total price of the items in the shopping cart is ${total:.2f}")


def view_cart(items, prices):
    if len(items) > 0:
        print("\nThe contents of the shopping cart are:")
        for i in range(len(items)):
            print(f"{i + 1} {items[i]} - ${prices[i]:.2f}")
    else:
        print("\nYour cart is empty.")


### SHOPPING CART ###
def shopping_cart():
    items = []
    prices = []

    print("Welcome to the Shopping Cart Program!\n")

    while True:
        menu()
        choice = input("\nPlease enter an action: ")
        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= 5:
                if choice == 1:
                    add_item(items, prices)
                elif choice == 2:
                    view_cart(items, prices)
                elif choice == 3:
                    remove_item(items, prices)
                elif choice == 4:
                    total(prices)
                elif choice == 5:
                    print("Thank you. Goodbye.")
                    break
            else:
                print("\nInvalid option. Please chose a number between 1 and 5.")
        else:
            print("\nInvalid option. Please try again.")



shopping_cart()