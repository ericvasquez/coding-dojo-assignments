class User:		
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0

    def make_deposit(self, amount):
    	self.account_balance += amount  # this method increases the user's by the amount specified
        
    def make_withdrawal(self, amount): # this method decreases the user's by the amount specified
        self.account_balance -= amount

    def display_user_balance(self):  # this method prints the user's name and account balance to the terminal
        print("User: " + self.name + ", Balance: $", self.account_balance)
 
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount 
        other_user.account_balance += amount 
        print("User: " + self.name + ", Balance: $", self.account_balance)
        print("User: " + other_user.name + ", Balance: $", other_user.account_balance)

#  Create 3 instances of the User class
someGuy = User("Some Guy", "someguy@python.com")
thisGuy = User("This Guy", "thisguy@python.com")
someOtherGuy = User("Some Other Guy", "someotherguy@python.com")

#  Have the first user make 3 deposits and 1 withdrawal and then display their balance
someGuy.make_deposit(1000)
someGuy.make_deposit(654)
someGuy.make_deposit(2)
someGuy.make_withdrawal(225)
someGuy.display_user_balance()

#  Have the second user make 2 deposits and 2 withdrawals and then display their balance
thisGuy.make_deposit(5000)
thisGuy.make_deposit(10)
thisGuy.make_withdrawal(675)
thisGuy.make_withdrawal(20)
thisGuy.display_user_balance()

#  Have the third user make 1 deposits and 3 withdrawals and then display their balance
someOtherGuy.make_deposit(200)
someOtherGuy.make_withdrawal(15)
someOtherGuy.make_withdrawal(7)
someOtherGuy.make_withdrawal(113)
someOtherGuy.display_user_balance()

# BONUS: transfer_money(self, other_user, amount) - have this method decrease the user's balance by the amount and add that amount to other other_user's balance
someGuy.transfer_money(someOtherGuy, 100)
