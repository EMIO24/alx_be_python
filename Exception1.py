num1 = int(input('Enter the numerator: '))
num2 = int(input('Enter the denomenator: '))
try:
    result = num1 / num2
    print(result)
except ZeroDivisionError:
    print('Your denomenator cannot be zero')
    