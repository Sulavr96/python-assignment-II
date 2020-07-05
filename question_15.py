class Customer:
    def __init__(self, first_name, last_name, account_number, balance):
        self.first_name = first_name
        self.last_name = last_name
        self.account_number = account_number
        self.balance = balance

    def full_name(self):
        return self.first_name + " " + self.last_name

    def account_info(self):
        return {'full_name': self.full_name(),
                'account_number': self.account_number,
                'current_balance': self.balance}

    def deposit(self, amount):
        self.balance += amount
        print("Deposit successful")

    def withdraw(self, amount):
        self.balance -= amount
        print("Withdraw successful")


customer1 = Customer('Suraj', 'Thapa', 123451321, 40000)
print(customer1.account_info())
customer1.deposit(20000)
customer1.withdraw(10000)
print(customer1.account_info())
