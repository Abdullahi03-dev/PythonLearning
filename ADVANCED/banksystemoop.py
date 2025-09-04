#A SIMPLE SIMPLE OOP FOR BANK SYSTEM
#self->this
#__init__->constructor
#---  -> new()





import random

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.account_number = random.randint(10000, 99999)  # auto-generate
        self.transactions = []  # store transaction history

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"Deposited {amount}")
        return f"Deposited {amount}. New balance: {self.balance}"

    def withdraw(self, amount):
        if amount > self.balance:
            self.transactions.append(f"Failed withdrawal of {amount} (Insufficient funds)")
            return "Insufficient funds!"
        self.balance -= amount
        self.transactions.append(f"Withdrew {amount}")
        return f"Withdrew {amount}. New balance: {self.balance}"

    def get_balance(self):
        return f"Account balance: {self.balance}"

    def get_transactions(self):
        return f"Transactions for {self.owner}: {self.transactions}"
        
        
        
acc1 = BankAccount("Abdullahi", 500)
print("Account Number:", acc1.account_number)

print(acc1.deposit(300))
print(acc1.withdraw(200))
print(acc1.withdraw(1000))
print(acc1.get_balance())
print(acc1.get_transactions())