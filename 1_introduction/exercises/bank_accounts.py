class BankAccount():
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
    def get_name(self):
        return self.name
    def get_balance(self):
        return self.balance
    def deposit(self, amount):
        self.balance += amount
        return self.balance
    def withdraw(self, amount):
        if amount <= self.balance:
            print('If you woke up broke, you should have never gone to sleep!')
        else:
            self.balance -= amount
            return self.balance
        