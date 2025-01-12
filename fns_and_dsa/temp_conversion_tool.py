FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
def convert_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius
def convert_to_fahrenheit(celsius):
    fahrenheit = celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32
    return fahrenheit

var1 = input('Enter the temperature to convert: ')
var = int(input('Please enter a numeric value. '))
var2 = input('Is this temperature in Celsius or Fahrenheit? (C/F): ')
if var2.upper() == 'F' and var1.upper() == 'CELSIUS':
    convert = convert_to_celsius(var)
    print(f'{var}°F is {convert}°C')
elif var2.upper() == 'C':
    convert = convert_to_fahrenheit(var)
    print(f'{var}°C is {convert}°F')
