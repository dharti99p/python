import random

# class Account :
#     balance = 5000
#     z = "Welcome to bank"
#     print(z.center(100,'-'))
#     print("Which Account is yours ? (Saving / Current) ")
#     ch = input("Enter your choice : ")

#     match ch :
#         case "Saving" :
#             z = "Your Account is Saving"
#             print(z.center(100,'-'))

#             a = input("Enter your name : ")
#             b = input("Enter your number : ")

#             print("Account Number : ",random.randint(1000000000000000,9999999999999999))
            
#             c = a[:5]
#             d = b[:5]
#             e = c + d
#             print("IFSC Number : ",e)
            
#             r = random.randint(1000, 9999)
#             print("Your Pin number :  ",r)
#             OLD_PIN = int(input("Plese Enter your PIN number : "))

#     def deposite(self) :
#         amount = float(input("Enter amount to be Deposited : "))
#         balance += selfamount
#         print("Amount Deposited : ",balance)

            
# aa = Account()
# aa.deposite()





    

class Account :
    def __init__(self) :
        self.balance = 5000
        z = "Welcome to bank"
        print(z.center(100,'-'))
        print("Which Account is yours ? (Saving / Current) ")
    
        ch = input("Enter your choice : ")
        match ch :
            case "Saving" :
                z = "Your Account is Saving"
                print(z.center(100,'-'))
                a = input("Enter your name : ")
                b = input("Enter your number : ")
                # amount = float(input("Enter amount to be Deposited : "))
                # self.balance += amount
                # print("Amount Deposited : ",self.balance)
                print("Account Number : ",random.randint(1000000000000000,9999999999999999))
                c = a[:5]
                d = b[:5]
                e = c + d
                print("IFSC Number : ",e)
                self.r = random.randint(1000, 9999)
                print("Your Pin number :  ",self.r)
                
            
                # def withdraw() :
                #     for i in range(3):
                #         if r == OLD_PIN :
                #             PIN = int(input("Enter the old PIN number : "))
                #             if PIN == OLD_PIN : 
                #                 r = random.randint(1000, 9999)
                #                 print("Your new PIN number : ",r)
                #                 NEW_PIN = int(input("Enter your NEW PIN number : "))
                #                 if NEW_PIN == r :
                #                     print("Done")
                #             else :
                #                 print("Your Pin number is Wrong. ")
                # withdraw()

            case "Current" :
                z = "Your Account is Current"
                print(z.center(100,'-'))
                a = input("Enter your name : ")
                b = input("Enter your number : ")
                amount = float(input("Enter amount to be Deposited : "))
                self.balance += amount
                print("Amount Deposited : ",amount)
                print("Account Number : ",random.randint(1000000000000000,9999999999999999))
                c = a[:5]
                d = b[:5]
                e = c + d
                print("IFSC Number : ",e)
    
    def deposite(self):
        ch = input("You choice deposite ! (YES / NO) -> ")
        match ch :
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
                  

aa = Account()
aa.deposite()


# # class Saving(Account) :
# #     def __init__(self) :
# #         Account.__init__(self)


# # class  Current(Account) :
# #     def __init__(self) :
# #         Account.__init__(self)

# # ss = Saving()
# # cc = Current()
