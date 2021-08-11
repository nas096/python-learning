class BankAccount:
    def __init__(self):
        self.flag = 0
        pass

    def get_balance(self):
        if self.flag == 1:
            return self.balance
        
        else:
            raise ValueError("Account closed")

    def open(self):
        if self.flag == 1:
            raise ValueError("Account already opened")
        self.flag = 1
        self.balance = 0
        # Check if this account open 2 times

    def deposit(self, amount):
        if self.flag == 0:
            raise ValueError("Account closed")

        if amount < 0:
            raise ValueError("Please enter an integer")

        self.balance += amount

    def withdraw(self, amount):
        if self.flag == 0:
            raise ValueError("Account Closed")
        
        if amount > self.balance:
            raise ValueError("Please enter a valid number")
        
        if amount < 0:
            raise ValueError("Please enter an integer")
        self.balance -= amount

    def close(self):
        # Check if this account already closed.
        if self.flag == 0:
            raise ValueError("Account already closed or you haven't opened the account yet.")

        self.flag = 0