class Atm:
    def __init__(self):
        self.user_create_pin = ""
        self.balance = 0
        self.manu()

    def manu(self):
        user_details = input(
            """
            1) Enter 1 to check pin
            2) Enter 2 to deposit
            3) Enter 3 to withdrew
            4) Enter 4 to check balance
            5) Enter 5 to exit

            """
        )
        if user_details == '1':
            self.create_pin()
        elif user_details == '2':
            self.deposit()
        elif user_details == '3':
            self.withdrew()
        elif user_details == " 4 ":
            self.check_balance()
        else:
            print(" Bye ")

    def create_pin(self):
        self.user_create_pin = int(input("Enter your pin:"))
        print("Your pin are successfully Created")

    def deposit(self):
        temp = int(input("Enter your pin:"))
        if temp == self.user_create_pin:
            amount = int(input("Enter Your Deposit Amount: $ "))
            self.balance = self.balance + amount
            print("Your account balance is: $ ", self.balance)
        else:
            print("Invalid pin")

    def withdrew(self):
        temp = int(input("Enter your pin:"))
        if temp == self.user_create_pin:
            amount = int(input("Enter Your Withdrew Amount: $ "))
            if amount < self.balance:
                self.balance = self.balance - amount
                print('Oreration Successful')
        else:
            print("insufficient Balance")
    
    def check_balance(self):
        temp = int(input("Enter your pin:"))
        if temp == self.user_create_pin:
            print("Your account balance is: $ ", self.balance)




Bkash = Atm() 
Bkash.deposit()
Bkash.withdrew()
Bkash.check_balance()
