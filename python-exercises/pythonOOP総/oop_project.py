from bank_accounts import *
from pythonAsync import *


Dave = BankAccount(1000, "Dave")
Sara = BankAccount(2000, "Sara")


Dave.getBalance()
Sara.getBalance()

Dave.deposit(500)

Dave.deposit(500)
Sara.withdraw(100)

Dave.transfer(1000, Sara)


Jim = InterestRewardsAcct(1000, "Jim")

Jim.getBalance()

Jim.deposit(100)

Jim.transfer(100, Dave)