k=65
a=1
n=int(input("enter the number "))
for i in range(1,n+1):
    for j in range(1,n+1):
        if((i+j)%2==0):
            print(" ",chr(k),end=" ")
            k+=1
        else:
            print(" ",a,end=" ")
            a+=1
    print( )
