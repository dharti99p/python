# 10.Python Program for n-th Fibonacci number 

a=0
b=1

n=int(input("Enter the number n : "))

for i in range(n+1):   
    print(a,end=" ")
    c=a+b
    a=b
    b=c