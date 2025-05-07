from datetime import datetime

current_day = datetime.now().weekday()
SALES_TAX_RATE = 0.06
DISCOUNT_RATE = 0.10
subtotal = 0
total_due = 0
discount_amount = 0
additional_amount_needed = 0

print('Enter the price and quantity for each item.')

while True:
    price = float(input('Please enter the price (enter 0 to finish): '))
    if price == 0:
        break
        
    quantity = int(input('Please enter the quantity: '))
    subtotal += price * quantity

if (current_day == 2 or current_day == 3) and subtotal >= 50:
    discount_amount = DISCOUNT_RATE * subtotal

sales_tax = SALES_TAX_RATE * (subtotal - discount_amount)
total_due = subtotal - discount_amount + sales_tax

if discount_amount > 0:
    print(f'Discount applied: ${discount_amount:.2f}')

print(f'Sales tax: ${sales_tax:.2f}')
print(f'Total to pay: ${total_due:.2f}')

if (current_day == 1 or current_day == 2) and subtotal < 50:
    additional_amount_needed = 50 - subtotal
    print(f'To receive the discount, add ${additional_amount_needed:.2f} to your order.')
