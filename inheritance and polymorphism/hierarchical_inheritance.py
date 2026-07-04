#banking system
class account:
    def __init__(self,ac_no,balance,name):
        self.ac_no=ac_no
        self.balance=balance
        self.name=name
    def show_balance(self):
        print("current balance: ",self.balance)
class savings_account(account):
    def add_intrest(self):
        intrest=self.balance*0.05
        self.balance+=intrest
        print("\n savings account")
        print("intrest added: ",intrest)
        print("balance: ",self.balance)
class current_account(account):
    def maintainance_charge(self):
        self.balance-=500
        print("\n current_account")
        print("maintainance_charge deducted is 500")
        self.show_balance()
s1=savings_account(1001,10009,"maya")
s1.add_intrest()
c1=current_account(1009,1324,"manyaa")
c1.maintainance_charge()
        