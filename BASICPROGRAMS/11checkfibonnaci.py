# 11.Python Program for How to check if a given number is Fibonacci number? 

a=1
b=1
c=0

n=int(input("Enter the number n : "))

if n==0 or n==1:
    print("This is fibonnaci number. ")
else:
    while(c<n):
        c=a+b
        b=a
        a=c
    if c==n:
        print("This is fibonnaci number.")
    else:
        print("This is not fibonnaci number.")