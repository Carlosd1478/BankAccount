class BankAccount:
    def __init__(self, balance=0.0, interest_rate=0.0):
        self.balance = balance
        if "%" in str(interest_rate):
            self.interest_rate = float(interest_rate.strip("%"))/100
        else:
            self.interest_rate = interest_rate
        # print(self.interest_rate)

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if self.balance - amount < 0:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        else:
            self.balance -= amount
            return self

    def display_account_info(self):
        print(f"Balance: ${self.balance}\nInterest Rate: {self.interest_rate}")
        return self

    def yield_interest(self):
        if self.balance > 0:
            self.balance += self.balance * self.interest_rate
        # print(self.balance)
        return self


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(balance= 5, interest_rate= 0.02)
        # print(self.account.balance)

        # other methods

    def make_deposit(self, amount):
        self.account.deposit(amount)
        # print(self.account.balance)

    def make_withdrawal(self, amount):
        self.account.withdraw(amount)

    def display_user_balance(self):
        userbalance = self.account.display_account_info()
        return userbalance


user1 = User("name", "hi@gmail.com")
account1 = BankAccount(10, "1%")
# account2 = BankAccount(20, "2%")

account1.deposit(10).deposit(10).deposit(10).withdraw(10).yield_interest().display_account_info()
# account2.deposit(120).deposit(20).withdraw(5).withdraw(20).withdraw(10).withdraw(4).yield_interest().display_account_info()


user1.make_deposit(200)
user1.make_withdrawal(10)
user1.display_user_balance()