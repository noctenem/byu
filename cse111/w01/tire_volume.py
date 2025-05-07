import math
from datetime import datetime

def tire_volume(width, aspect, diameter):
    return (math.pi * (width ** 2) * aspect) * (width * aspect + 2540 * diameter) / 10000000000  # Normalización correcta

def find_price(width, aspect, diameter):
    if width == 185 and aspect == 50 and diameter == 14:
        return 100.0 # fictitious price
    elif width == 205 and aspect == 60 and diameter == 15:
        return 120.0 # fictitious price
    elif width == 235 and aspect == 70 and diameter == 16:
        return 140.0 # fictitious price
    else:
        return 180.0 # default price

width = float(input('Enter the width of the tire in mm (e.g., 205): '))
aspect = float(input('Enter the aspect ratio of the tire (e.g., 60): '))
diameter = float(input('Enter the diameter of the wheel in inches (e.g., 15): '))

volume = tire_volume(width, aspect, diameter)

print(f'The approximate volume is {volume:.2f} liters')

price = find_price(width, aspect, diameter)
print(f'The price for the selected tire size is ${price:.2f}')

buy_tires = input('Do you want to buy tires with these dimensions? (yes/no): ')

if buy_tires.lower() == 'yes' or buy_tires.lower() == 'y':
    phone_number = input('Please enter your phone number: ').strip()


    current_date = datetime.now().strftime('%Y-%m-%d')

    with open('volumes.txt', 'at') as file:
        file.write(f'{current_date}, {int(width)}, {int(aspect)}, {int(diameter)}, {volume:.2f}, ${price:.2f}, (+{phone_number[0]}) {phone_number[1:]}\n')

    print('Your information has been saved.')    

else:
    print('Thank you for using our service!')