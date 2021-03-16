class BankAccount:
    def __init__(self, int_rate=0.01, balance=0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if amount > self.balance:
            self.balance -= 5
            print("Insufficient funds: Charging a $5 fee")
        else:    
            self.balance -= amount
        return self

    def display_account_info(self):
        print("Balance: $", self.balance)
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += (self.balance * self.int_rate)
        return self

first = BankAccount()
second = BankAccount(.02, 100)

first.deposit(500).deposit(22).deposit(13).withdraw(114).yield_interest().display_account_info()
second.deposit(25).deposit(77).withdraw(22).withdraw(11).withdraw(5).withdraw(7).yield_interest().display_account_info()


