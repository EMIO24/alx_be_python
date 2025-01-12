FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5
def convert_to_celsius(fahrenheit):
    celsius = fahrenheit - 32 / FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius
def convert_to_fahrenheit(celsius):
    fahrenheit = celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + 32
    return fahrenheit

var1 = float(input('Enter the temperature to convert: '))
var2 = input('Is this temperature in Celsius or Fahrenheit? (C/F): ')
if var2.upper() == 'F':
    convert = convert_to_celsius(var1)
    print(f'{var1}°F is {convert}°C')
elif var2.upper() == 'C':
    convert = convert_to_fahrenheit(var1)
    print(f'{var1}°C is {convert}°F')
