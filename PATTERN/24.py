k=65
a=65
n=int(input("enter the number "))
for i in range(1,n+1):
    for j in range(1,n+1):
        if(j%2==1):
            print(" ",chr(k),end=" ")
            k+=1
        else:
            print(" ",a,end=" ")
            a+=1
    print( )