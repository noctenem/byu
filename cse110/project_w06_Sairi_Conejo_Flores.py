"""
Program: Data Analysis
Author: Sairi Conejo Flores

Purpose: create a program that shows the minimum, maximun an
         average life expectancy.
"""
# Introduced a featured that asks the user to type a country and
# then displays the minimum, maximun and average life expectancy

def load_data(filename):
    data = []
    with open(filename) as file:
        for line in file:
            data.append(line.strip().split(","))

    return data

def find_extremes(data):
    # variable initialization
    min_life = float("inf")
    max_life =  -float("inf")
    min_info = None
    max_info = None

    for row in data[1:]: # avoid the header
        life = float(row[3])

        if life < min_life:
            min_life = life
            min_info = row

        if life > max_life:
            max_life = life
            max_info = row

    return min_life, min_info, max_life, max_info

def get_year(data, year):
    countries = []
    total_life = 0

    for row in data[1:]: # avoid the header
        if row[2].isdigit() and int(row[2]) == year:
            countries.append(row)
            total_life += float(row[3])

    # variable initialization
    min_life = float("inf")
    max_life =  -float("inf")
    min_info = None
    max_info = None
    avg_life = 0

    for country in countries:
        life = float(country[3])

        if life < min_life:
            min_life = life
            min_info = country

        if life > max_life:
            max_life = life
            max_info = country

    if countries:
        avg_life = total_life / len(countries)
    else:
        avg_life = 0

    return avg_life, min_info, max_info

def largest_drop(data):
    country_years = {}
    largest_drop_value = 0
    country_with_largest_drop = None

    for row in data[1:]: # avoid the header
        country = row[0]
        year = int(row[2])
        life_expectancy = float(row[3])

        if country not in country_years:
            country_years[country] = {}

        country_years[country][year] = life_expectancy

    for country, years in country_years.items():
        sorted_years = sorted(years.keys())

        for i in range(1, len(sorted_years)):
            year1 = sorted_years[i-1]
            year2 = sorted_years[i]
            drop = years[year1] - years[year2]

            if drop > largest_drop_value:
                largest_drop_value = drop
                country_with_largest_drop = (country, year1, year2)

    return largest_drop_value, country_with_largest_drop

def country_analysis(data, country_name):
    country_data = []

    for row in data[1:]:
        if row[0] == country_name:
            country_data.append(row)

    if not country_data:
        print(f"No data available for {country_name}")
        return
    
    min_life = float("inf")
    max_life = -float("inf")
    total_life = 0

    for row in country_data:
        life = float(row[3])
        total_life += life

        if life < min_life:
            min_life = life

        if life > max_life:
            max_life = life

    avg_life = 0
    if country_data:
        avg_life = total_life / len(country_data)
    else:
        avg_life = 0

    print(f"""
Country: {country_name}
The average life expectancy was: {avg_life:.2f}
The overall min life expectancy is: {min_life}
The overall max life expectancy is: {max_life}
""")

def data_analysis():
    print("\nData Analysis\n")
    year = int(input("Enter the year of interest: "))

    data = load_data("life-expectancy.csv")

    min_life, min_info, max_life, max_info = find_extremes(data) # unpacking

    print(f"The overall min life expectancy is: {min_life} from {min_info[0]} in {min_info[2]}")
    print(f"The overall max life expectancy is: {max_life} from {max_info[0]} in {max_info[2]}")

    drop, country_drop = largest_drop(data)
    if country_drop:
        print(f"\nLargest drop in life expectancy: {drop} for {country_drop[0]} from {country_drop[1]} to {country_drop[2]}")

    avg_life, min_info, max_info = get_year(data, year) # unpacking

    print(f"""
For the year {year}:
The average life expectancy across all countries was: {avg_life:.2f}
The min life expectancy was in {min_info[0]}: {min_info[3]}
The max life expectancy was in {max_info[0]}: {max_info[3]}
""")
    
    country_name = input("\nEnter a country to analyze: ").capitalize()
    country_analysis(data, country_name)
    

data_analysis()