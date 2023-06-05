class BankAccount:

    def __init__(self, interest_rate, balance):
        self.interest_rate = interest_rate
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"\nYou have just deposited ${amount}.\nYour current balance is now ${self.balance}.\n")
            return self
        print("\nYou have tried to deposit an invalid amount of dinero.\n")
        return(self)

    def withdraw(self, amount):
        if amount > 0:
            if self.balance - amount >= 0:
                self.balance -= amount
                print(f"\nYou have successfully withdrawn ${amount}.\nYour current balance is now ${self.balance}.\n") 
            else:
                print(f"You have insuffucient funds for this transaction.\nYou can not withdraw ${amount} with a ${self.balance} balance.\nYour current balance is still ${self.balance}.\nYour transaction was declined.\n")
        return self

    def display_account_info(self):
        print(f"\nYour current account balance is ${self.balance}.\nThe interest rate on this account is {self.interest_rate}%\n")
        return self

    def yield_interest(self):
        self.balance *= (1 + self.interest_rate)
        print(f"After an interest yield of {self.interest_rate}%, your new balance is ${self.balance}.\n")
        return self

john, tammy = BankAccount(0.01, 100), BankAccount(0.03, 400)

john.deposit(100).deposit(40).deposit(900).yield_interest().display_account_info()
tammy.deposit(1).deposit(2).deposit(3).withdraw(10).withdraw(11).withdraw(100).withdraw(tammy.balance + 4).display_account_info()