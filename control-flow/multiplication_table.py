number = int(input('Enter a number to see its multiplication table: '))
for i in range(1, 11):
    mul = number * i
    print(f'{number} * {i} = {mul}')