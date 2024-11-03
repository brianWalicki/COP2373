# This program stores account information as a BankAcct object.
# It then has multiple methods to print out information.

# Defines the class BankAcct and its variables
class BankAcct:
    def __init__(self, name, account_num, funds, rate, days):
        self.name = name
        self.account_num = account_num
        self.funds = funds
        self.rate = rate
        self.days = days

    # Overwrites __str__ to print balance and interest
    def __str__(self):
        return (f'Current Balance: ${self.funds:.2f}\n'
                f'Current interest {self.rate:.2f}')

    # Changes object's interest rate
    def adjust_rate(self, new_rate):
        self.rate = new_rate

    # Withdraws specified money from object's fund variable (if possible)
    def withdraw(self, amount):
        if amount <= self.funds:
            self.funds -= amount
        else:
            print('insufficient funds')

    # Adds funds to object's fund variable
    def deposit(self, amount):
        self.funds += amount

    # Returns object's balance
    def get_balance(self):
        return self.funds

    # Calculates the interest due depending on interest and days
    def calc_interest(self, days):
        interest = self.funds * (self.rate * (days / 365))
        self.funds += interest
        return interest


# Test function to see that all the methods in BankAcct work
def test(name, account_num, funds, rate, days):
    # Defines a new instance of type BankAcct
    test_acc = BankAcct(name, account_num, funds, rate, days)

    # Tests all different functions in BankAcct in order
    print(test_acc)
    BankAcct.adjust_rate(test_acc, .3)
    BankAcct.withdraw(test_acc, 20)
    print(test_acc)
    BankAcct.deposit(test_acc, 10)
    print(test_acc)
    print(test_acc.get_balance())
    print(f'Interest owned, ${test_acc.calc_interest(365)}')


test('jake', 1111, 10000, .1, 300)
