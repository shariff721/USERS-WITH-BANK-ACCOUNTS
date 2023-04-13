
class BankAccount:

    all_accounts = []

    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)


    def deposit(self,amount):
        self.balance += amount
        return self


    def withdraw(self,amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient Funds")
        return self



    def display_account_info(self):
        print(f" Interest Rate: {self.int_rate}\n Account Balance: {self.balance}")
        return self


    def yield_interest(self):
        self.balance += self.int_rate*self.balance
        return self
    
    @classmethod
    def print_all_instances(cls):
        for account in cls.all_accounts:
            print(account.balance)
            print(account.int_rate)



class User:
    def __init__(self,name,email):
        self.name = name
        self.email = email
        self.checkingaccount = BankAccount(int_rate = 0.5,balance = 0)
        self.savingsaccount = BankAccount(int_rate = 0.05,balance = 50)
        

    def display_info(self):
        print(f" Name: {self.name}\n Email: {self.email}")
        return self


    def make_deposit(self,amount,account):
        if account == "checkingaccount":
            self.checkingaccount.deposit(amount)
        elif account == "savingsaccount":
            self.savingsaccount.deposit(amount)
        return self


    def make_withdraw(self,amount,account):
        if account == "checkingaccount":
            self.checkingaccount.withdraw(amount)
        elif account == "savingsaccount":
            self.savingsaccount.withdraw(amount)
        return self
    
    def display_user_balance(self):
        print(f"{self.name}'s Account Balance:")
        print(f" Checking Account Balance: {self.checkingaccount.balance}")  
        print(f" Savings Account Balance: {self.savingsaccount.balance}")  
        return self
    
    # def transfer_money(self,amount,other_user):
    #     other_user


sharif = User("muyanja", "smuyanja04@gmail.com")
maryam = User("maryam", "maryamayah10@gmail.com")



sharif.make_deposit(1000,"checkingaccount").make_withdraw(200,"checkingaccount").display_user_balance()
maryam.display_user_balance()