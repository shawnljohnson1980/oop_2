class User:
    def __init__(self, name_input, email_input):
        self.name=name_input
        self.email=email_input
        self.account_balance=0.0

    def make_deposit(self, amount):
            self.account_balance +=amount
            return self
        
    def venmo (self, amount, payee):
            self.account_balance -=amount
            payee.account_balance +=amount
            return self
    def make_widthdrawl(self, amount):
        self.account_balance -= amount
        return self
        
shawn = User("Shawn","shawn@mail.com")
andrew= User ("Andrew","andrew@mail.com")


shawn.make_deposit(700).venmo(500, andrew).make_deposit(100).make_deposit(200).make_deposit(300).make_widthdrawl(50)
print(f"Shawn's Account balance: ${shawn.account_balance} ")
print(f"Andrews account balance: ${andrew.account_balance}")