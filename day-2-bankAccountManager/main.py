class Account:

    def __init__(self,name,password,balance=0):
        self.name = name
        self.balance = balance
        self.password = password
        self.history = [] # List to store all transactions
        if(balance>0):
            self.history.append({"type":"deposit","amount":balance})

    def verify_password(self):
        pwd = input("Enter password: ")
        return pwd==self.password
    
    def deposit(self,money):
        if not self.verify_password():
            print("INCORRECT PASSWORD")
            return

        self.balance += money
        trans = {"type":"deposit","amount":money}
        self.history.append(trans)
        print(f"Deposited {money}. New Balance: {self.balance}")

    def withdraw(self,amount):
        if not self.verify_password:
            print("INCORRECT PASSWORD")
            return
        if amount <= self.balance:
            self.balance-=amount
            self.history.append({"type":"withdraw","amount":amount})
            print(f"Withdrew {amount}. Remaining Balance: {self.balance}")
        else:
            print("Insufficient Balance")


    def add_interest(self,rate):
        """ Add Interest to the balance """
        interest = self.balance * (rate/100)
        self.balance += interest
        self.history.append({"type":"interest","amount":interest})

    def show_history(self):
        for txn in self.history:
            print(txn)
        
    def check_balance(self):
        if not self.verify_password():
            print("INCORRECT PASSWORD")
            return
        print(f"{self.name}'s balance: {self.balance}" )

    
accounts = []

def create_account():
    name = input("Enter your name: ")
    balance = float(input("Enter initial balance: "))
    password = input("Enter password: ")

    acc = Account(name,password,balance)
    accounts.append(acc)
    print("Account created successfully! ")

def find_account(name):
    for acc in accounts:
        if acc.name == name:
            return acc
        return None


create_account()


acc = find_account("sagar")
if acc:
    acc.deposit(1000)
    acc.withdraw(500)
    acc.add_interest(5)
    acc.show_history()
