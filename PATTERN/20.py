k=65
n=int(input("enter the number "))
for i in range(1,n+1):
    for j in range(1,n+1):
        if(i%2==1):
            print(" ",chr(k),end=" ")
        else:
            print(" ",chr(k+32),end=" ")
        k+=1
    print( )