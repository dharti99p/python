import random

user=0

while True :
    
    user = int(input("Enter your number : "))
    
    cnumber = random.randint(0,10)
    print("Computer Number : ",cnumber)

    if user > cnumber :
        # print("Computer Number : ",cnumber)
        print("Your guess number is too high...")
    elif user < cnumber :
        # print("Computer Number : ",cnumber)
        print("Your guess number is too low...")
    else : 
            # print("Computer Number : ",cnumber)
        print("Your guess number is equal...")
        break

print("Thanks for Playing !")                               
