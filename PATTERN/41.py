n=int(input("enter the number :"))
for i in range(1,n+1):
    for j in range(1,n+1):
       if(i>=j ):
            print(i-j+1,end=" ")
       else:
            print(" ",end=" ")
    print( )