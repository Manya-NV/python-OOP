class bank_account:
    def __init__(self,acnt_no,balance):
        self.acnt_no=acnt_no
        self.__balance=balance
    def deposit(self,amt):
        self.__balance+=amt
        print(f"available balance {self.__balance} and deposit ammount is {amt}")
    def withdraw(self,amt):
        if self.__balance>amt:
            self.__balance-=amt
            print(f"amount withdrawn is {amt} and remaining balance {self.__balance}")
        else:
            print("insufficient balance") 
b=bank_account(1001023,5000)
b.deposit(1000)
b.withdraw(300)
