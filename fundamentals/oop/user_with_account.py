from bank_account import BankAccount

class User:

    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = {"checking": BankAccount(interest_rate = 0.02, balance = 1000),
                         "savings": BankAccount(interest_rate = 0.05, balance = 500.00),
                         "money_market": BankAccount(interest_rate = 0.10, balance = 5000)}

    def make_deposit(self, account, amount):
        return self.accounts[str(account)].deposit(amount)

    def make_withdrawal(self, account, amount):
        return self.accounts[str(account)].withdraw(amount)
    
    def display_user_balance(self, account):
        return self.accounts[str(account)].display_account_info()

    def transfer_money(self, other_user, source_account, amount, target_account):
        other_user.make_deposit(target_account, amount)
        self.make_withdrawal(source_account, amount)
        print(f"\n{self.name} has successfully sent ${amount} to {other_user.name}.\n")    
        return self



anthony = User("anthony", "anthony@email.com")
shakira = User("shakira", "shakira@email.com")

anthony.transfer_money(shakira, "checking", 500, "savings")