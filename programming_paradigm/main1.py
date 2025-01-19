import sys
from bank_account import BankAccount

def main():
    account = BankAccount(100)  # Example starting balance
    command = input('Enter your input: ')
    amount = float(input('Enter the amount: '))
    if command == "deposit" and amount is not None:
        account.deposit(amount)
        print(f"Deposited: ${amount}")
    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient funds.")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()