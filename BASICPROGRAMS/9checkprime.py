# 9. Python program to check whether a number is Prime or not 

n=int(input("enter the number : "))

f=0

for i in range(2,n):
    if(n%i==0):
        f=1

if(f==0):
    print("prime number ")
else:
    print("not prime number ")