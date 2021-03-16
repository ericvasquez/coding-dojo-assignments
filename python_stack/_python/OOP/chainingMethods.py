# Update your previous assignment so that each instance's methods are chained
class User:		
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawal(self, amount): 
        self.account_balance -= amount
        return self


    def display_user_balance(self):  
        print("User: " + self.name + ", Balance: $", self.account_balance)
        return self

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount 
        other_user.account_balance += amount 
        print("User: " + self.name + ", Balance: $", self.account_balance)
        print("User: " + other_user.name + ", Balance: $", other_user.account_balance)
        return self

someGuy = User("Some Guy", "someguy@python.com")
thisGuy = User("This Guy", "thisguy@python.com")
someOtherGuy = User("Some Other Guy", "someotherguy@python.com")

someGuy.make_deposit(1000).make_deposit(654).make_deposit(2).make_withdrawal(225).display_user_balance()

thisGuy.make_deposit(5000).make_deposit(10).make_withdrawal(675).make_withdrawal(20).display_user_balance()

someOtherGuy.make_deposit(200).make_withdrawal(15).make_withdrawal(7).make_withdrawal(113).display_user_balance()

someGuy.transfer_money(someOtherGuy, 100)
