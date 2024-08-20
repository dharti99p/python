n=int(input("enter the number "))
for i in range(1,n+1):
    for j in range(1,n+1):
        if(i%2==1):
            print("1",end=" ")
        else:
            print("0",end=" ")
    print( )