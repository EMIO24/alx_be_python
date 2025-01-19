import sys
from robust_division_calculator import safe_divide

def main():
    numerator = input('Enter a number: ')
    denominator = input('Enter a number: ')

    result = safe_divide(numerator, denominator)
    print(result)

if __name__ == "__main__":
    main()