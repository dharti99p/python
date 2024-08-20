n=input("Enter the number : ")

print("your number : ",n)

for i in n :
    i=int(i)
    # print(i)
    if i>=4:
        i-=4
        print("E",end=" ")
    else:
        print("-",end=" ")

    if i>=2:
        i-=2
        print("W",end=" ")
    else:
        print("-",end=" ")
    
    if i>=1:
        i-=1
        print("R",end=" ")
    else:
        print("-",end=" ")