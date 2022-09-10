class BankAccount:
    all_accounts_list =[]

    def __init__(self, int_rate, balance):
        BankAccount.all_accounts_list.append(self)
        self.int_rate = int_rate
        self.balance = balance
    
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

class User: 
    def __init__ (self, name, email, chk_balance, sav_balance):
        self.name = name
        self.email = email
        self.checking = BankAccount(.02, chk_balance)
        self.savings = BankAccount(.04, sav_balance)

    def make_deposit(self, account_type, amount):
        if (account_type == "checking"):
            self.checking.deposit(amount)
        elif (account_type == "savings"):
            self.savings.deposit(amount)

    def make_withdrawal(self, account_type, amount):
        if (account_type == "checking"):
            self.checking.withdraw(amount)
        elif (account_type == "savings"):
            self.savings.withdraw(amount)

    def display_user_balance(self, account_type):
        if (account_type == "checking"):
            print(f"{self.name}'s checking balance is: ${self.checking.balance:.2f}")
        elif (account_type == "savings"):
            print(f"{self.name}'s savings balance is: ${self.savings.balance:.2f}")

    def transfer_money(self, amount, other_user):
        self.checking.withdraw(amount)
        other_user.checking.deposit(amount)


# TEST BELOW #

# create users:
new_user1 = User("Adam", "Adam@all.com",100,0)
new_user2 = User("Eve", "Eve@all.com",0,200)

#display current balances for user1 to make sure creating users worked. 
new_user1.display_user_balance("checking")
new_user1.display_user_balance("savings")
new_user2.display_user_balance("checking")
new_user2.display_user_balance("savings")


#deposit to user 1 and show new balance
new_user1.make_deposit("checking",250)
new_user1.display_user_balance("checking")


#make a transfer of $44 from user1 to user2.
new_user1.transfer_money(44, new_user2)

#show user1 and user2's new balances to verify the transfer actually worked. 
new_user1.display_user_balance("checking")
new_user2.display_user_balance("checking")




