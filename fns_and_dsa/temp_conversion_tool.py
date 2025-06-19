FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_celsius(fahrenheit):
    global FAHRENHEIT_TO_CELSIUS_FACTOR
    result = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return result

def convert_to_fahrenheit(celsius):
    global CELSIUS_TO_FAHRENHEIT_FACTOR
    result = celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32
    return result

user_input = float(input("Enter the temperature to convert: "))
ask_input = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
if ask_input == 'C':
    print(f"{user_input}°C is {convert_to_fahrenheit(user_input)}°F")
elif ask_input == 'F':
    print(f"{user_input}°F is {convert_to_celsius(user_input)}°C")
else:
    print("Invalid temperature. Please enter a numeric value.")
