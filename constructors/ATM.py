class ATM:
    def __init__(self,balance=0):
        self.balance=balance
    def deposit(self,amt):
        self.balance+=amt
        print(f"available balance {self.balance} and deposit ammount is {amt}")
    def withdraw(self,amt):
        if self.balance>amt:
            self.balance-=amt
            print(f"amount withdrawn is {amt} and remaining balance {self.balance}")
        else:
            print("insufficient balance") 
b=ATM(5000)
b.deposit(1000)
b.withdraw(300)

        