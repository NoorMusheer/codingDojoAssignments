class BankAccount:
    instances = []
    def __init__(self, int_rate, balance):
        self.instances.append(self)
        self.int_rate = int_rate
        self.balance = 0.00
    
    def deposit(self, amount):
        self.balance = self.balance + amount
        return self

    def withdraw(self, amount):
        if (self.balance < amount):
            print("Insufficient funds: Charging a $5 fee.")
            self.balance = self.balance - 5.00
        else: 
            self.balance = self.balance - amount
        return self

    def display_account_info(self):
        print(f"Balance : $ {self.balance:.2f}")
        return self
    
    def yield_interest(self):
        if (self.balance >= 0):
            self.balance = (self.balance)*(1.00 + self.int_rate)
        return self

    @classmethod
    def all_instances(cls):
        print(cls.instances)


customer1 = BankAccount(0.05, 0.00)
customer2 = BankAccount(0.10, 0.00)

customer1.deposit(50).deposit(75).withdraw(30).yield_interest().display_account_info()
customer2.deposit(500).deposit(345).withdraw(50).withdraw(40).withdraw(30).withdraw(20).yield_interest().display_account_info()

BankAccount.all_instances()
