'''Mini Project:

Write a python program to replicate a Banking system. The following features are mandatory:
1.Account login
2. Amount Depositing
3. Amount Withdrawal
Other than the above features you can add any other also.
'''
class BankAccount:
    def __init__(self, name, ifsc_code, account_no, balance, username, password):
        self.name = name
        self.ifsc_code = ifsc_code
        self.account_no = account_no
        self.balance = balance
        self.username = username
        self.password = password
        self.transactions = []

    def display_balance(self):
        print(f"Account Balance: ${self.balance}")

    def display_transactions(self):
        print("Transaction History:")
        for transaction in self.transactions:
            print(transaction)

class AccountLogin:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    def display(self):
        print(f"Username: {self.username}\nPassword: [Hidden for security]")

class AmountDeposit(BankAccount):
    def __init__(self, name, ifsc_code, account_no, balance, username, password, deposited_amount):
        super().__init__(name, ifsc_code, account_no, balance, username, password)
        self.deposited_amount = deposited_amount

    def process_deposit(self):
        if self.deposited_amount > 0:
            self.balance += self.deposited_amount
            self.transactions.append(f"Deposited ${self.deposited_amount}")
            print(f"Deposited ${self.deposited_amount}.")
            self.display_balance()
        else:
            print("Invalid deposit amount.")

class AmountWithdrawal(BankAccount):
    def __init__(self, name, ifsc_code, account_no, balance, username, password, amount_to_withdraw):
        super().__init__(name, ifsc_code, account_no, balance, username, password)
        self.amount_to_withdraw = amount_to_withdraw

    def process_to_withdraw(self):
        print(f"Enter the amount to withdraw: {self.amount_to_withdraw}")
        if self.amount_to_withdraw > 0 and self.amount_to_withdraw <= self.balance:
            self.balance -= self.amount_to_withdraw
            self.transactions.append(f"Withdrew ${self.amount_to_withdraw}")
            print(f"Withdrew ${self.amount_to_withdraw}.")
            self.display_balance()
        else:
            print("Invalid withdrawal amount or insufficient funds.")

# Get user input
name = input("Enter your name: ")
ifsc_code = input("Enter the IFSC code: ")
account_no = input("Enter your account number: ")

# Get user input securely for password
password = input("Enter your password: ")

# Confirm password
confirm_password = input("Confirm your password: ")
while password != confirm_password:
    print("Passwords do not match. Please try again.")
    password = input("Enter your password: ")
    confirm_password = input("Confirm your password: ")

# Create instances with user input
user_account = BankAccount(name, ifsc_code, account_no, 0, name.lower(), password)  # Starting with zero balance

# Display initial information
print(f"\nInitial Information:")
print(f"Name: {user_account.name}")
print(f"Account Number: {user_account.account_no}")
print(f"Balance: ${user_account.balance}")

# Perform transactions # Break the loop if input is matches
while True:
    try:
        initial_balance = float(input("Enter the initial balance: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid numerical value for the initial balance.")

# Set the initial balance
user_account.balance = initial_balance

# Display updated initial information
print("\nUpdated Initial Information:")
print(f"Name: {user_account.name}")
print(f"Account Number: {user_account.account_no}")
print(f"Balance: ${user_account.balance}")

# Perform transactions
deposit_amount = float(input("Enter the amount to deposit: "))
deposit_transaction = AmountDeposit(name, ifsc_code, account_no, initial_balance, name.lower(), password, deposit_amount)
deposit_transaction.process_deposit()

withdrawal_amount = float(input("Enter the amount to withdraw: "))
withdrawal_transaction = AmountWithdrawal(name, ifsc_code, account_no, initial_balance, name.lower(), password, withdrawal_amount)
withdrawal_transaction.process_to_withdraw()
