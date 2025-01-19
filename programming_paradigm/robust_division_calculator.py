try:
    def safe_divide(numerator, denominator):
        result = numerator / denominator
        print(f'The result of the division is {result}')
except ValueError:
    print("Error: Please enter numeric values only.")
except NameError:
    print("Error: Please enter numeric values only.")
except TypeError:
    print("Error: Please enter numeric values only.")
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
