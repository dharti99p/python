import random

class Account :
    name, mobile_no, pin_no = '', 0, 0
    def __init__(self) : 
        self.name = input("Enter your name : ")
        self.mobile_no = input("Enter your mobile number : ")
        print("Account Number : ",random.randint(1000000000000000,9999999999999999))
        self.c = self.name[:5]
        self.d = self.mobile_no[:5]
        self.e = self.c + self.d
        print("IFSC Number : ",self.e)
        self.r = random.randint(1000, 9999)
        print("Your Pin number :  ",self.r)
    
    def set_pin(self):
        self.ch = input("You change your PIN no ? (YES / NO) -> ")
        match self.ch :
            case "YES" :
                for i in range(3) :
                    self.old_pin = int(input("Enter The Pin::=>"))
                    if(self.old_pin == self.r):
                        self.r = int(input("Enter Your New Pin::=>"))
                        print("Your new PIN number : ",self.r)
                    else:
                        print("Your Pin is Wrong")

    def deposite(self):
        self.ch = input("You choice deposite ! (YES / NO) -> ")
        match self.ch :
            case "YES" :
                for i in range(3):
                    self.OLD_PIN = int(input("Plese Enter your PIN number : "))
                    if self.r == self.OLD_PIN :
                        amount = float(input("Enter amount to be Deposited : "))
                        self.balance += amount
                        print("Amount Deposited : ",self.balance)
                        break
                    else:
                        print("Your Pin number is Wrong.")
                else:
                    print("Your Account is Block For Next 24.")

    def withdraw(self):
        self.ch = input("You choice Withdraw ! (YES / NO) -> ")
        match self.ch :
            case "YES" :
                for i in range(3):
                    self.OLD_PIN = int(input("Plese Enter your PIN number : "))
                    if self.r == self.OLD_PIN :
                        amount = float(input("Enter amount to be Withdraw : "))
                        self.balance -= amount
                        print("Amount Deposited : ",self.balance)
                        break
                    else:
                        print("Your Pin number is Wrong.")
                else:
                    print("Your Account is Block For Next 24.")


class Saving(Account) :
    def __init__(self) :
        Account.__init__(self)
        self.balance = 5000
        z = "Your Account is Saving"
        print(z.center(100, '-'))
        print("your account is saving availabel balance 5000rs : ")

class Current(Account) :
    def __init__(self) :
        Account.__init__(self)
        self.balance = 10000
        z = "Your Account is Current"
        print(z.center(100,'-'))
        print("your account is current availabel balance 10000rs : ")


ss = Saving()
ss.set_pin()
ss.deposite()
ss.withdraw()

cc = Current()
ss.set_pin()
cc.deposite()
cc.withdraw()