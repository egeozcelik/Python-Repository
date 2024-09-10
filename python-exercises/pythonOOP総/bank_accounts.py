class BalanceException(Exception):
    pass 

class BankAccount:
    def __init__(self, initialAmount, accName):
        self.balance = initialAmount
        self.name = accName
        print(f"\nAccount '{self.name}' created. \nBalance ${self.balance:.2f}") 

    
    def getBalance(self):
        print(f"\nAccount '{self.name}' balance = ${self.balance:.2f}")

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"\nDeposit complete.")
        self.getBalance()

    
    def viableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(#özel olarak tanımlanmış bir hata verdirmek. 
                f"\nSorry, account {self.name} only has balance of ${self.balance:.2f}"
            )
    
    def withdraw(self, amount):
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount
            print("\Withdraw complete.")
            self.getBalance()
        except BalanceException as error:
            print(f'\nWithdraw interrupted: {error}')

    def transfer(self, amount, account):
        try:
            print('\n*********\n \nBeggining Transfer..')#initialize
            self.viableTransaction(amount)#control
            self.withdraw(amount)#decrease money
            account.deposit(amount)#append money
            print('\nTransfer Complete!\n\n**********')#inform
        except BalanceException as error:
            print(f'\nTransfer interrupted.\n')#error


class InterestRewardsAcct(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance + (amount * 1.05)
        print("\nDeposit Complete.")
        self.getBalance()