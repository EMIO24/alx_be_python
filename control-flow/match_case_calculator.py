#!/bin/python3
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
ope = input("Choose the operation (+, -, *, /): ")
match ope:
    case "+":
        result = num1 + num2
        print(f"The result is {result}")
    case "-":
        result = num1 - num2
        print(f"The result is {result}")
    case "*":
        result = num1 * num2
        print(f"The result is {result}")
    case "/":
        if num1 == 0 or num2 == 0:
            print("Cannot divide by zero.")
        else:
            result = num1 / num2
            print(f"The result is {result}")
    case _:
        print("I cannot help you out.")
