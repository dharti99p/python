# ₹
import datetime
import random

print("       HOTEL MANAGEMENT SYSTEM       ")

def check(a):
    if "YES" == a:
        return True
    elif "NO" == a:
        return False
    
a = input("if you are enter the HOTEL press YES otherwise NO : ")

tf = check(a)
# print(tf)
print("1.AC Room")
print("2.NON-AC Room")
print("3.VIP Room")
print("4.Semi-VIP Room")
i=1
if tf:
    r = random.randint(1000,9999)
    print("Your vacation Enjoy OTP number : ",r)
    OTP = int(input("Enter your OTP number : "))

    if r == OTP:
        nm = input("Enter your name : ")
        rv = int(input("Enter your room number : "))
        match rv :
            case 1 :
                z = "You Selected AC Room"
                print(z.center(100,"-"))
                time = {
                    "Hourly" : [210, "1%"],
                    "Quterly" : [1250, "2%"],
                    "Dayly" : [5000, "4%"],
                    "Weekly" : [35000, "5%"],
                    "Monthly" : [150000, "6%"]
                }
                tk = []
                tv = []
                for k, v in time.items():
                    print(f"{i}. {k} : {v}")
                    i += 1
                    tk.append(k)
                    tv.append(v)
                rtv = int(input("Enter the type : "))
                match rtv:
                    case rtv:
                        z = "You Selected Your Plan"
                        print(z.center(100,"-"))
                        if rtv <= 5 :

                            price = tv[rtv -1][0]
                            ret = tv[rtv -1][1]
                            print(f"Price is {price} and Ret is {ret}")                 
                            dt = datetime.datetime.now()
                            d = datetime.datetime.strftime(dt,"%d %b %Y   %H:%M:%S.%f")
                            date=d.split()
                            print(date)
            case 2 :
                z = "You Selected Non-AC Room"
                print(z.center(100,"-"))
                time = {
                    "Hourly" : [167, "1%"],
                    "Quterly" : [1000, "2%"],
                    "Dayly" : [4000 ,"4%"],
                    "Weekly" : [28000, "5%"],
                    "MonthLY" : [120000, "6%"]      
                }
                tk = []
                tv = []
                for k,v in time.items() : 
                    print(f"{i}. {k} : {v}")
                    i += 1
                    tk.append(k)
                    tv.append(v)
                rtv = int(input("Enter the type : "))
                match rtv :
                    case rtv :
                        z = "You Selected Your Plan"
                        if rtv <= 5 :
                            price = tv[rtv -1][0]
                            ret = tv[rtv -1][1] 
                            print(f"Price is {price} and Ret is {ret}")
                            dt = datetime.datetime.now()
                            d = datetime.datetime.strftime(dt,"%d %b %Y   %H:%M:%S.%f")
                            date=d.split()
                            print(date)

            case 3 :
                z = "You Selected VIP Room"
                print(z.center(100,"-"))
                time = {
                    "Hourly" : [292, "1%"],
                    "Quterly" : [1750, "2%"],
                    "Dayly" : [7000, "4%"],
                    "Weekly" : [49000, "5%"],
                    "Monthly" : [210000, "6%"]
                }
                tk = []
                tv = []
                for k, v in time.items() :
                    print(f"{i}. {k} : {v}")
                    i += 1
                    tk.append(k)
                    tv.append(v)
                rtv = int(input("Enter the type : "))
                match rtv :
                    case rtv :
                        z = "You Selected Your Plan"
                        if rtv <= 5:
                            price = tv[rtv -1][0]
                            ret = tv[rtv -1][1]
                            print(f"Price is {price} and Ret is {ret}")
                            dt = datetime.datetime.now()
                            d = datetime.datetime.strftime(dt,"%d %b %Y   %H:%M:%S.%f")
                            date=d.split()
                            print(date)

            case 4 : 
                z = "You Selected Semi VIP Room"
                print(z.center(100,"-"))
                time = {
                    "Hourly" : [250, "1%"],
                    "Quterly" : [1500, "2%"],
                    "Dayly" : [6000, "4%"],
                    "Weekly" : [42000, "5%"],
                    "Monthly" : [180000, "6%"]
                }
                tk = []
                tv = []
                for k, v in time.items() : 
                    print(f"{i}. {k} : {v}")
                    i += 1
                    tk.append(k)
                    tv.append(v)
                rtv = int(input("Enter the type : "))
                match rtv :
                    case rtv : 
                        z = "You Selected Your Plan"
                        print(z.center(100,"-"))
                        if rtv <=5 :
                            price = tv[rtv -1][0]
                            ret = tv[rtv -1][1]
                            print(f"Price is {price} and Ret is {ret}")
                            dt = datetime.datetime.now()
                            d = datetime.datetime.strftime(dt,"%d %b %Y   %H:%M:%S.%f")
                            date=d.split()
                            print(date)
                            

def check_out(a) :
    if "YES" == a :          
        return True
    elif "NO" == a : 
        return False

a = input("you are OUT the HOTEL press YES : ")

check_out(a)

if tf :
    ynm=input("you are press yes and plese your name : ")
    
    if nm == ynm : 
        print("Your bill is : ",rv)
        


    