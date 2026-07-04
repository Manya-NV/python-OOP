class payment:
    def pay(self,amount):
        pass
class credit_card:
    def pay(self,amount):
        print(f"paid {amount} using credit card")
class upi:
    def pay(self,amount):
        print(f"paid {amount} using upi")
class net_banking:
    def pay(self,amount):
        print(f"paid {amount} using credit card")
class cash:
    def pay(self,amount):
        print(f"paid {amount} using cash")
payment=[
    credit_card(),
    upi(),
    net_banking(),
    cash()
]
for p in payment:
    p.pay(500)