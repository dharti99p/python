n=int(input("enter the number "))
for i in range(n):
    for j in range(n):
        if(i%2==0):
            num=(n*i)+j+1
            print(" ",num,end=" ")
        else:
            num=(n*(i+1))-j
            print(" ",num,end=" ")
    print( )