"""
Program: Windchill Calculator
Author: Sairi Conejo Flores

Purpose: Program that displays wind chill values for various wind speeds
         for a temperature.
"""

def calculate_wind_chill(temperature, wind_speed):
    return 35.74 + (0.6215 * temperature) - 35.75 * (wind_speed ** 0.16) + 0.4275 * temperature * (wind_speed ** 0.16)

def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def main():
    temp = float(input("What is the temperature?: "))
    scale = input("Fahrenheit or Celsius (F/C)?: ").upper()

    if scale == "C":
        temp = celsius_to_fahrenheit(temp)

    for wind_speed in range(5, 65, 5):
        wind_chill = calculate_wind_chill(temp, wind_speed)
        print(f"At temperature {temp:.1f}F, and wind speed {wind_speed} mph, the windchill is: {wind_chill:.2f}F")

main()