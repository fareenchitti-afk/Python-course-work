#.Abstraction 

from abc import ABC, abstractmethod

class BankAccount(ABC):
    def Checkbalance(self,username):
        self.username=username
        print(f"\n\nHi {self.username}!1\nDisplay the balance")

    @abstractmethod
    def deposit(self):
        pass

    @abstractmethod
    def withdraw(self):
        pass


class CurrentAccount(BankAccount):
    def deposit(self):
        print("Anytime time deposit")
    def withdraw(self):
        print("No limits")
    

class SavingAccount(BankAccount):
    def deposit(self):
        print("NO limits for deposit")
    def withdraw(self):
        print("We have limits per day")

class SalaryAccount(BankAccount):
    def deposit(self):
        print("Deposit once in a month")
    def withdraw(self):
        print("NO limits, charges are applied")

class JointAccount(BankAccount):
    def deposit(self):
       print("2 of them can deposit")
    def withdraw(self):
       print("No limit, both can withdraw")

class PensionAccount(BankAccount):
    def deposit(self):
       print("Once in a month")
    def withdraw(self):
       print("20K per day")

class FixedDepositAccount(BankAccount):
    def deposit(self):
        print("One time deposit")
    def withdraw(self):
       print("Once in a year")

fareen = CurrentAccount()
rama = SavingAccount()
priya = SalaryAccount()
aara = JointAccount()
reena = PensionAccount()
varsha = FixedDepositAccount()

fareen.Checkbalance("fareen")
fareen.deposit()
fareen.withdraw()

rama.Checkbalance("rama")
rama.deposit()
rama.withdraw()

priya.Checkbalance("priya")
priya.deposit()
priya.withdraw()

aara.Checkbalance("aara")
aara.deposit()
aara.withdraw()

reena.Checkbalance("reena")
reena.deposit()
reena.withdraw()

varsha.Checkbalance("varsha")
varsha.deposit()
varsha.withdraw()



