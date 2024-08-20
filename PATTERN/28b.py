n=int(input("enter the number "))
for i in range(2,n):
    p=1
    for j in range(2,n):
        if(i%j==0):
            p=0
    if(p):
        print(" ",i,end=" ")
    else:
        print(" ",end=" ")
    print()