import csv
from datetime import datetime, timedelta

# Added reminder of days until new year, 30 deay return date,
# 50% BOGO discount for D0983 and coupon printing for
# a purchased product

# CONSTANTS
SALES_TAX_RATE = 0.06

def read_dictionary(filename, key_column_index):
    dictionary = {}

    with open(filename, 'r', newline='') as csv_file:
        reader = csv.reader(csv_file)

        next(reader)
        for row in reader:
            if len(row) == 0:
                continue

            key = row[key_column_index]
            product_number = row[0]
            product_name = row[1]
            price = float(row[2])
            dictionary[key] = [product_number, product_name, price]

    return dictionary

def days_until_new_year():
    today = datetime.now()
    next_year = datetime(year = today.year + 1, month = 1, day = 1)
    delta = next_year - today
    return delta.days

def return_by_date():
    now = datetime.now()
    return_date = now + timedelta(days = 30)
    # Set the time to exactly 9 PM
    return return_date.replace(hour = 21, minute = 0, second = 0, microsecond = 0)

def main():

    try:
        products_dict = read_dictionary('products.csv', 0)
        print('Inkom Emporium')

        total_items = 0
        subtotal = 0

        # save ordered products for coupon later 
        products_ordered = []
        
        with open('request.csv', 'r', newline='') as request_file:
            reader = csv.reader(request_file)
            next(reader)

            for row in reader:
                if len(row) == 0:
                    continue

                product_number = row[0]
                quantity = int(row[1])

                product_info = products_dict[product_number]
                product_name = product_info[1]
                product_price = product_info[2]

                # Apply BOGO 50% discount only for D083
                if product_number == 'D083':
                    full_price_quantity = (quantity +1) // 2
                    half_price_quantity = quantity // 2
                    line_total = (full_price_quantity * product_price) + (half_price_quantity * product_price * 0.5)
                    subtotal += line_total
                    total_items += quantity

                    print(f'{product_name}: {quantity} @ {product_price:.2f} (BOGO 50% applied)')
                    print(f'line total: ${line_total:.2f}')
                else:
                    line_total = quantity * product_price
                    subtotal += line_total
                    total_items += quantity
                    
                    print(f'{product_name}: {quantity} @ {product_price:.2f}')


                products_ordered.append(product_name)

        sales_tax = subtotal * SALES_TAX_RATE
        total = subtotal + sales_tax

        print(f'Number of Items: {total_items}')
        print(f'Subtotal: {subtotal:.2f}')
        print(f'Sales Tax {sales_tax:.2f}')
        print(f'Total: {total:.2f}')
        print(f'Thank you for shopping at the Inkom Emporium.')

        current_date_and_time = datetime.now()
        print(f'{current_date_and_time:%a %b %d %H:%M:%S %Y}')

        days_left = days_until_new_year()
        print(f'Reminder: {days_left} days until the new years sale begins!')

        ret_date = return_by_date()
        print(f'Return by: {ret_date:%a %b %d %I:%M %p}')

        if products_ordered:
            coupon_product = products_ordered[0]
            print(f'COUPON: Save 10% on your next purchase of {coupon_product}!')

    except FileNotFoundError as file_err:
        print('Error: missing file',)
        print(file_err)
    except PermissionError as perm_err:
        print('Error: permission denied')
        print(perm_err)
    except KeyError as key_err:
        print('Error: unknown product ID in the request.csv file')
        print(key_err)


if __name__ == '__main__':
    main()