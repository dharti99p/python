k=96
n=int(input("enter the number "))
for i in range(n):
    for j in range(n):
        if(i%2==0):
            num=(n*i)+j+1
            print(" ",chr(k+num),end=" ")
        else:
            num=(n*(i+1))-j
            print(" ",chr(k+num),end=" ")
    print( )